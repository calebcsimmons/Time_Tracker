 ## Script to Record Time
 ## Owner: Caleb Simmons
 ## Origin: 10/23/2023
 ## Last Updated: 10/23/2023

import os
import datetime

# Get the current date and time when the script is run
# This script is set to run each morning when the computer is turned on
current_time = datetime.datetime.now()
current_date = current_time.date()
time_only = current_time.time()
time_only = time_only.strftime("%H:%M %p")

# Print the turn-on time
print("Computer turn-on time:", current_time)

# Generate the filename for the current date
path = "C:\\Caleb Simmons\\Scripts\\Time Tracker\\timestamps"
os.makedirs(path, exist_ok=True)  # Create the directory if it doesn't exist
filename = os.path.join(path, f"{current_date}.txt")

# Open the file for appending
with open(filename, 'a') as file:
    # Write the turn-on time to the file
    file.write("Date: " + str(current_date) + "\n" "\n")
    file.write("Shift Started: " + str(time_only) + "\n")
    file.close()
    
print(f"Turn-on time saved to {filename}")