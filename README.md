# Battery Alert
![Text Notification](./resources/text_alert_linux.png "Text notification")

This program will maintain a log of battery percentage and notify users using text and voice notifications. 

# Motivation
In Ubuntu 20.04, I was not getting any low battery notifications. My laptop was shutting down suddenly without any alert. I tried to use many tweaks from the Internet though nothing worked perfectly. Annoyed with the problem, I have created *Battery Alert*, a simple lightweight and customizable application for measuring battery percentage after a specific time interval.     

# Features
The application has the following features - 
1. Maintains a log file with battery percentage, charging status, duration after a specific percentage change in battery status.
2. Shows a text alert when battery percentage is below a certain threshold and it is not charging.
3. Sends a sound alert when the battery percentage is below a certain threshold and it is not charging.
4. Shows alerts when battery is charged fully.
5. Runs on Windows and Linux (Not tested in Mac)

# Why to use?
1. If your laptop's battery is faulty and you want to measure battery capacity.
2. If you want to get notifications after a certain threshold of your laptop's battery.
3. If you want to keep track battery's charging time and discharging time.
4. If you want to keep track of the rate of discharging.
5. If you want to get alerts after your laptop's battery is charged fully.
6. Something else

# How to use it?

Go to your terminal and run it as simple as the following - 
```
python3 battery_alert.py
```
You can also customize the default parameters by doing the following -
```
python3 battery_alert.py --sleep_time=300 --log_percentage=1 --alert_percentage=20 --notification_alert=True --sound_alert=True 
```
All the parameters are shown above with default values. You can customize them as you want. 

# Parameters
1. **sleep_time** : (Datatype = Integer). Interval (in seconds) to check for the battery percentage. E.g, `sleep_time=300` means the application will be activated after every 300 seconds (5 minutes).

2. **log_percentage** : (Datatype = Integer). Writes an entry in the log file after every *log_percentage* difference in battery status. E.g, `log_percentage=1` means the application will add an entry after every 1% of change in battery status.

3. **alert_percentage** : (Datatype : Integer). The application starts sending text and/or sound alerts after *alert_percentage*. E.g, `alert_percentage = 20` means, the application will send text and/or sound notifications when your laptop's battery has 20% of charge and it is not charging.

4. **notification_alert** : (Datatype : Boolean). Whether to enable or disable text notification. E.g, `notification_alert = True` means, the text notification is enabled. 

5. **sound_alert** : (Datatype : Boolean). Whether to enable or disable the sound notification. E.g, `sound_alert = True` means, the sound notification is enabled.

# Log file
When the program is executed, the current time and date will be added in the log file named *battery_alert.log*. This date and time are considered as *base time*. Then it adds a log entry after every *log_percentage* apart as discussed above. The log entry will have four comma-separated values- 
> battery percentage, Whether charging or not, Time between every entry, Total time from base time to the current entry

![Log File](./resources/log.png "Log File")

E.g, Here the base date and time is 25th September 2021 at 11:38 pm. The third entry describes after 10 minutes from base time and after 5 minutes from the previous entry, the battery percentage was 77% and it is not charging.

# Installation

## Step 1 
Clone the repository by
```
git clone https://github.com/duttaprasanta/battery_alert.git
```
You may also download the zip file.

![Download zip file](./resources/download_zip.png "Download zip file")

Then extract it.

## Step 2

### For Linux

#### Requirements
This app requires the below 3 
1. python3-pip
2. gcc
3. espeak
4. libdbus-glib-1-dev, libdbus-1-dev (for ubuntu)

For the installation of the above packages use the below command -
```
<package manager> install <package name>
``` 
For example for ubuntu it should be as follows-

```
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install gcc
sudo apt-get install espeak
sudo apt-get install libdbus-glib-1-dev libdbus-1-dev
```
Then install the pip dependencies as follows-
```
pip install --upgrade pip
pip install -r requirements_linux.txt
```
### For Windows
```
pip install --upgrade pip
pip install -r requirements_windows.txt
```
If you face dependency conflicts, create a virtual environment and follow the above steps. You may also try the tested-dependencies - requirements_linux_legacy.txt/ requirements_windows_legacy.txt

### Test the installation
**First unplug the charger from your laptop. Then execute the below command -**
```
python3 battery_alert.py --log_percentage=1 --alert_percentage=100 --sleep_time=0
```
You should see a text notification and hear a sound alert upon successful execution of the above command. 

## Step 3 (If you want to run the program at system startup)

### For Linux
Create an entry in the *Startup Application* app
```
python3 /home/<your_user_name>/battery_alert.py
```
![Startup](./resources/startup_linux.png "Startup")

### For Windows
Run the following command:
```
python win_autostart.py
```
A file named ```battery_alert.vbs``` will be generated. Now you paste the shortcut of that file inside the following folder
```
C:\Users\<WindowsUserName>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

![Windows Startup Location](./resources/win_startup_location.png "Windows Startup Location")

> **Notes** 
1. Replace `<WindowsUserName>` with your user name.
2. By default `AppData` file is hidden. To view that click on `View` > `Hidden items` on File Explorer.
3. If you want to change the default parameters of the program, you need to change that inside the generated file named `win_autostart.bat` also.

# Some useful links
Project Website : [https://duttaprasanta.github.io/battery_alert](https://duttaprasanta.github.io/battery_alert)

Project Link : [https://github.com/duttaprasanta/battery_alert](https://github.com/duttaprasanta/battery_alert)

Email : prasanta7dutta@gmail.com

# Support
If you like this repository, kindly :star: it and follow me.

# Want to contribute?
1. **Fork** this repository
2. Modify it
3. Create a **Pull request**
