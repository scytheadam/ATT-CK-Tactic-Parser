import argparse
import json
import requests
import stix2


def get_data_from_branch(domain, branch="master"):
    dest = "https://raw.githubusercontent.com/" \
        "mitre/cti/{}/{}/{}" \
        ".json".format(branch, domain, domain)
    stix_json = requests.get(dest).json()
    return stix2.MemoryStore(stix_data=stix_json["objects"])


if __name__ == '__main__':
    print("Running...\n")
    # Setup Arguments ...
    parser = argparse.ArgumentParser()
    '''
    Example File:

    https://raw.githubusercontent.com/scythe-io/community-threats/93f4e07c6792499153be2702f4f8ea23c3666cb9/Orangeworm/orangeworm_layer.json
    '''
    parser.add_argument(
        '--jsonfile', required=True,
        help='''
            The target ATT&CK Navigator JSON file. Can be local file or URL.
        ''',
    )
    parser.add_argument(
        '--mitigations', action='store_true',
        help='''
            Optional ability to print all the mitigations for the TID.
        ''',
    )
    args = parser.parse_args()
    # Load custom layer JSON
    # First, try for a local file
    try:
        with open(args.jsonfile) as f:
            custom_layer = json.load(f)
    except (FileNotFoundError, IsADirectoryError, OSError):
        try:
            custom_layer = requests.get(args.jsonfile).json()
        except requests.exceptions.MissingSchema as e:
            print(
                "Error: could not find '{}' local/URL!".format(args.jsonfile)
            )
            print(e)
            print("\n ...Exiting.\n")
            exit()
        except ValueError as e:
            # Catch JSONDecodeError too ...
            print(
                "Error: bad JSON via '{}' URL!".format(args.jsonfile)
            )
            print(e)
            print("\n ...Exiting.\n")
            exit()
    # Load ATT&CK Data from internet
    src = get_data_from_branch("enterprise-attack")
    # Gather data into single object
    data = {}
    for technique in custom_layer['techniques']:
        # Query for Technique information
        cur_tec = src.query([
            stix2.Filter(
                "external_references.external_id", "=",
                technique['techniqueID']
            ),
            stix2.Filter("type", "=", "attack-pattern")
        ])[0]
        # Get the Tactic
        cur_tactic = cur_tec["kill_chain_phases"][0]["phase_name"]
        # Sort by tactic
        if data.get(cur_tactic) is None:
            data[cur_tactic] = []
        data[cur_tactic].append(
            (
                technique['techniqueID'],
                cur_tec["name"],
                cur_tec['x_mitre_detection']
            )
        )
    # End FOR
    # Present Data ...
    for tactic in data:
        # Remove Duplicates
        data[tactic] = list(dict.fromkeys(data[tactic]))
        # Print Results
        print("\n{}".format(tactic.title()))
        for technique in data[tactic]:
            print("{} - {}".format(technique[0], technique[1]))
            if args.mitigations:
                print("Mitigations - {}\n".format(technique[2]))
        # End technique FOR
    # End tactic FOR
    # Done!
    print("\n ...Exiting.\n")
    exit()
