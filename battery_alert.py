import psutil					# For getting battery info
from plyer import notification	# For showing text notification
from datetime import datetime	# For getting date and time
import time						# For measuring duration 
import pyttsx3					# For text to speech
import argparse					# For Argument Parser


# User Inputs
parser = argparse.ArgumentParser(description="Enter args")
parser.add_argument('--sleep_time', required=False, help='How long the app to sleep',default=5 * 60, type=int)
parser.add_argument('--log_percentage', required=False, help='Logging frequency (in percentage difference)',default=1, type=int)
parser.add_argument('--alert_percentage', required=False, help='When to alert (at which percentage)',default=20, type=int)
parser.add_argument('--notification_alert', required=False, help='Enable/ Disable text notification',default=True, type=bool)
parser.add_argument('--sound_alert', required=False, help='Enable/ Disable sound notification',default=True, type=bool)
args = parser.parse_args()



# Parameters
sleep_time = args.sleep_time # Time to sleep (in seconds)
log_percentage = args.log_percentage # Log when log_percentage (%) of change is observed
alert_percentage = args.alert_percentage # Minimum percentage to alert
notification_alert = args.notification_alert # Enable or disable text notification alert
sound_alert = args.sound_alert	# Enable or disable sound notification alert


# Initializing Text to Speech engine
engine = pyttsx3.init()
now = datetime.now()	# Current Date and time 

# Adding data and time in the log
log = open('battery_alert.log','a')	
log.write('\n\n--------------------------------\n')
log.write(f'{now}\n')
log.write('--------------------------------\n')
log.close()

# Getting battery info 
battery = psutil.sensors_battery()	
old_percent = battery.percent

old_time = time.time()
base_time = old_time
first = True

while(True):
	# Getting battery info
	battery = psutil.sensors_battery()
	current_percent = battery.percent
	plugged = battery.power_plugged

	# True when difference between current and old percentage >= log_percentage or first time
	if(first or abs(old_percent-current_percent) >= log_percentage):
        # Logging
		log = open('battery_alert.log','a')
		cur_time = time.time()
		log.write(f'{round(current_percent)},{plugged},{round((cur_time-old_time)/60)} min., {round((cur_time-base_time)/60)} min.\n')
		log.close()
		# Updating variables
		old_time = cur_time
		old_percent = current_percent
		first = False

		# True when alert is enabled and current percentage <= threshold and not charging
		if (notification_alert==True and current_percent<=alert_percentage and plugged==False):
		    
		    # Text notification
		    notification.notify(
		        title = 'Bettery Percentage',
		        message = str(round(current_percent)) + '%',
		        app_name = 'Battery Alert',
		        timeout = 1,
		        #ticker = str(round(current_percent)) + '%',
		        toast = False
		    )
		
		# True when sound alert is enabled and current percentage <= threshold and not charging
		if(sound_alert==True and current_percent <= alert_percentage and plugged==False):
		    # Sound Notification
			engine.say(f"Battery percentage {round(current_percent)} %")
			engine.runAndWait()
		
    # Sleep the app for sometime
	time.sleep(sleep_time)
