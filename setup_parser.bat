@echo off
rem See if python is already in the path
for /f "usebackq tokens=*" %%a in (`where python`) do set pypath=%%a

if not defined pypath (
        rem unset pypath in the case of an error, so checking if it's defined below works. This is an ugly hack.
        set "pypath="
        rem pypath not found. Check in the registry
        for /f "tokens=3" %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\Python.exe"  /ve ^|findstr /ri "REG_SZ"') do set pypath=%%a
)

if not defined pypath (
        rem Also not in the registry. Try the default location.
        if exist C:\Python38\python.exe (set pypath="C:\Python38\python.exe")
)

if not defined pypath (
        rem still no path. Terminate.
        @echo can't find python location. Terminating.
        exit /B 1
)

@echo on
%pypath% -m venv .\venv
call ".\venv\Scripts\activate.bat"
pip install -r requirements.txt
python attack_json_to_bullets.py --help
cmd /k
