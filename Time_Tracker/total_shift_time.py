 ## Total Shift Time Calculator

import os
import datetime

# Get the current date and time when the script is run
current_time = datetime.datetime.now()
current_date = current_time.date()
time_only = current_time.time()
time_only = time_only.strftime("%H:%M %p")

# Generate the filename for the current date
path = "C:\\Caleb Simmons\\Scripts\\Time Tracker\\timestamps"
os.makedirs(path, exist_ok=True)  # Create the directory if it doesn't exist
filename = os.path.join(path, f"{current_date}.txt")


#Parse Through Lines for Data
with open(filename, 'r') as file:
    lines = file.readlines()
    start_time_str = lines[2]
    end_time_str = lines[3]
    file.close()
    
start_time = start_time_str.split(':')
start_time_part = start_time[2].split()
