from sys import platform        # For detecting OS
import os

if platform == "win32":    # Windows OS
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

    print("Registry values:--\nvalue name: batteryAlertApp\nvalue data: ", vbs_path, "\n")