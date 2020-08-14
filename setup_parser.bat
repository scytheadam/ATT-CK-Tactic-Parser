@echo off
rem Change the path to Python3 that works for you!
rem Example:
rem C:\Users\User\AppData\Local\Microsoft\WindowsApps\python.exe -m venv .\venv
@echo on
C:\Python38\python.exe -m venv .\venv
call ".\venv\Scripts\activate.bat"
pip install -r requirements.txt
python attack_json_to_bullets.py --help
cmd /k
