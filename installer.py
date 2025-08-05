import os
import PyInstaller
print("Welcome to the installer!!\nThis will install the netstrike script compatible with your system\n")

if os.name == 'nt':
    os.system('powershell -Command "Invoke-WebRequest -Uri \'https://raw.githubusercontent.com/Holy-Pentagram/NetStrike/refs/heads/main/netstrike\' -OutFile \'netstrike.py\'"')
    os.system("pip install pyinstaller")
    os.system("pyinstaller --onefile --name netstrike netstrike.py")
elif os.name == 'posix':
    os.system("curl -o netstrike https://raw.githubusercontent.com/Holy-Pentagram/NetStrike/refs/heads/main/netstrike")
    os.system("chmod +x netstrike")
    os.system("sudo mv netstrike /usr/bin/netstrike")
else:
    print("Sorry but your operating system isn't supported, please send a request at my github and I would be happy to implement it.")