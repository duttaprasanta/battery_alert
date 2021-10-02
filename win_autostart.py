from sys import platform        # For detecting OS
import os

# Checks for Windows OS(both 32 & 64 bit)
if platform == "win32": 
    # generate battery_alert.bat script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    py_abs_path = '"' + os.path.join(dir_path, 'battery_alert.py') + '"\n'
    script = "python " + py_abs_path

    # Creating the .bat file
    bat_path = os.path.join(dir_path, 'win_autostart.bat')
    with open(bat_path, 'w') as fp:
        fp.write("@echo off\n")
        fp.write(script)
        fp.write("@pause\n")

    # Creating the .vbs file
    vbs_path = os.path.join(dir_path, 'battery_alert.vbs')
    with open(vbs_path, 'w') as fp:
        temp = 'CreateObject("Wscript.Shell").Run "win_autostart.bat", 0, True'
        fp.write(temp)
    print('Operation Completed Successfully...')
    
# Check for Linux OS		
elif platform.startswith("linux"):
    print('Linux OS is detected.\nThis code is only for Windows OS.')

# Check for MAC OS	
elif platform == "darwin":
    print('Mac OS is detected.\nThis code is only for Windows OS.')
