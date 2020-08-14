ATT&CK Tactic Parser
=========

Input a custom ATT&CK Navigator Layer; Outputs a list of Techniques grouped by Tactic.


Initial Setup
-----
### Requires

- Python3
- pip
- virtualenv
- A URL to a ATT&CK Navigator Layer

### Steps

#### On Windows

Simply double click ``setup_parser.bat`` and run using,

(venv) > ``python attack_json_to_bullets.py --jsonfile ... ``

#### Otherwise ...

1. Create virtual environment.

    (On OSX or Linux)
    $ ``python3 -m venv ./venv``

    (On Windows)
    $ ``C:\Python38\python.exe -m venv .\venv``

0. Enter virtual environment.

    (On OSX or Linux)
    $ ``source ./venv/bin/activate``

    (Windows)
    $ ``.\venv\Scripts\activate.bat``

0. Install required python libs.

    (venv) $ ``pip install -r requirements.txt``


Example Usage
-----

```
(venv) $ python attack_json_to_bullets.py --jsonfile https://raw.githubusercontent.com/scythe-io/community-threats/93f4e07c6792499153be2702f4f8ea23c3666cb9/Orangeworm/orangeworm_layer.json
Running...


Discovery
T1087 - Account Discovery
T1087.001 - Local Account
T1087.002 - Domain Account
T1083 - File and Directory Discovery
T1135 - Network Share Discovery
T1201 - Password Policy Discovery
T1069 - Permission Groups Discovery
T1069.002 - Domain Groups
T1069.001 - Local Groups
T1057 - Process Discovery
T1018 - Remote System Discovery
T1082 - System Information Discovery
T1016 - System Network Configuration Discovery
T1049 - System Network Connections Discovery
T1033 - System Owner/User Discovery
T1007 - System Service Discovery
T1124 - System Time Discovery

Command-And-Control
T1071 - Application Layer Protocol
T1071.001 - Web Protocols
T1008 - Fallback Channels
T1105 - Ingress Tool Transfer

Execution
T1059 - Command and Scripting Interpreter
T1059.003 - Windows Command Shell
T1569 - System Services
T1569.002 - Service Execution

Persistence
T1136 - Create Account
T1136.001 - Local Account
T1136.002 - Domain Account
T1543 - Create or Modify System Process
T1543 - Create or Modify System Process
T1543.003 - Windows Service
T1543.003 - Windows Service

Defense-Evasion
T1140 - Deobfuscate/Decode Files or Information
T1070 - Indicator Removal on Host
T1070.004 - File Deletion
T1070.005 - Network Share Connection Removal
T1036 - Masquerading
T1036.004 - Masquerade Task or Service
T1027 - Obfuscated Files or Information
T1027.001 - Binary Padding
T1218 - Signed Binary Proxy Execution
T1218.011 - Rundll32

Lateral-Movement
T1570 - Lateral Tool Transfer
T1021 - Remote Services
T1021.002 - SMB/Windows Admin Shares

 ...Exiting.

```
