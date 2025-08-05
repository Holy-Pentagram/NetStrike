import platform
import os

try:
    # Try automatic detection first
    if platform.system() == 'Darwin':
        os.system("curl -o netstrike.py https://raw.githubusercontent.com/Holy-Pentagram/NetStrike/refs/heads/main/netstrike")
        os.system("pip install pyinstaller")
        os.system("pyinstaller --onefile --name netstrike netstrike.py")
    elif os.name == 'nt':
        os.system('powershell -Command "Invoke-WebRequest -Uri \'https://raw.githubusercontent.com/Holy-Pentagram/NetStrike/refs/heads/main/netstrike\' -OutFile \'netstrike.py\'"')
        os.system("pip install pyinstaller")
        os.system("pyinstaller --onefile --name netstrike netstrike.py")
    elif os.name == 'posix':
        os.system("curl -o netstrike.py https://raw.githubusercontent.com/Holy-Pentagram/NetStrike/refs/heads/main/netstrike")
        os.system("pip install pyinstaller")
        os.system("pyinstaller --onefile --name netstrike netstrike.py")
        os.system("sudo mv dist/netstrike /usr/local/bin/")
    else:
        raise Exception("OS not automatically detected")
        
except Exception as e:
    print("Automatic installation failed. Let's try manual installation.")
    os_choice = input('What is your operating system?\n1. Windows\n2. Linux\n3. MacOS\nEnter your choice: ')
    
    if os_choice == '1' or os_choice.lower() == 'windows':
        print("Don't worry, I will help you solve it by manually installing it.")
        print("Just copy paste these commands into your terminal:")
        print('1. paste: powershell -Command "Invoke-WebRequest -Uri \'https://raw.githubusercontent.com/Holy-Pentagram/NetStrike/refs/heads/main/netstrike\' -OutFile \'netstrike.py\'"')
        print("2. paste: pip install pyinstaller")
        print("3. paste: pyinstaller --onefile --name netstrike netstrike.py")
    elif os_choice == '2' or os_choice.lower() == 'linux':
        print("Don't worry, I will help you solve it by manually installing it.")
        print("Just copy paste these commands into your terminal:")
        print("1. paste: curl -o netstrike.py https://raw.githubusercontent.com/Holy-Pentagram/NetStrike/refs/heads/main/netstrike")
        print("2. paste: pip install pyinstaller")
        print("3. paste: pyinstaller --onefile --name netstrike netstrike.py")
        print("4. paste: sudo mv dist/netstrike /usr/local/bin/")
    elif os_choice == '3' or os_choice.lower() == 'macos':
        print("Don't worry, I will help you solve it by manually installing it.")
        print("Just copy paste these commands into your terminal:")
        print("1. paste: curl -o netstrike.py https://raw.githubusercontent.com/Holy-Pentagram/NetStrike/refs/heads/main/netstrike")
        print("2. paste: pip install pyinstaller")
        print("3. paste: pyinstaller --onefile --name netstrike netstrike.py")
    else:
        print("We're very sorry, but we do not support your operating system yet.")
        print("Please leave a comment under the GitHub page and I would be happy to add support for it!")