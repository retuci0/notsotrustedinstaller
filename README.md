# not so trusted installer (ignore the icon)

basic python and powershell program to run stuff as trusted installer

trusted installer is the maximum set of privileges in a windows machine

works by starting the desired process as a child of the `TrustedInstaller` process, giving you its set of privileges

if you only want to run as `SYSTEM` (aka LocalSystem) for some reason, just use PsExec with the -s flag

if you don't need the gui and want to use it as a cli instead, use the powershell script as follows:

`./ti.ps1 -executableName <executableName>`

to verify you are running as ti, run `whoami /groups`

somewhere, it should say `NT SERVICE\TrustedInstaller`

however, if you just run `whoami` it will return `nt authority\system`, because SYSTEM is the user account,
and TrustedInstaller is just a set of privileges the SYSTEM account can have

the script requires to be run with administrator privileges

## how to run

- `git clone https://github.com/retuci0/notsotrustedinstaller.git`
- `cd notsotrustedinstaller`
- `python -m venv .env` <- highly recommended to start a virtual enviroment
- `./.env/Scripts/activate.ps1` for powershell
- `.env\Scripts\activate.bat` for command prompt (cmd)
- `pip install -r requirements.txt`
- `python main.py` or `python3 main.py` depending on your python installation

## credits
to whoever originally wrote the powershell script

i only found it sitting on my pc and did some slight modifications but

i think i originally found it in reddit so credits to that reddit guy
