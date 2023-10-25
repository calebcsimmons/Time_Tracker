 ## Script to Record Time
 ## Owner: Caleb Simmons
 ## Origin: 10/23/2023
 ## Last Updated: 10/25/2023

import os
import datetime

# Get the current date and time when the script is run
current_time = datetime.datetime.now()
current_date = current_time.date()
time_only = current_time.strftime("%H:%M %p")

# Generate the filename for the current date
path = "C:\\Caleb Simmons\\Scripts\\Time Tracker\\timestamps"
os.makedirs(path, exist_ok=True)  # Create the directory if it doesn't exist
filename = os.path.join(path, f"{current_date}.txt")

# Read the existing content of the file or create the file if it doesn't exist
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    lines = []

# Modify Line 3
if len(lines) >= 4:
    lines[3] = "Shift Ended: " + str(time_only) + "\n"
else:
    lines.append("Shift Ended: " + str(time_only) + "\n")

# Write the modified content back to the file
with open(filename, 'w') as file:
    file.writelines(lines)
