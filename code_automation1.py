import os

# Start of the program
print("Scanning all files in the clients_sites folder...")

# Get the full path of the current script
script_path = os.path.abspath(__file__)

# Extract the directory where the script is located
script_dir = os.path.dirname(script_path)

# Define the path to the clients_sites folder
base_path = os.path.join(script_dir, "clients_sites")

# Traverse through all files in the clients_sites folder
for root, _, files in os.walk(base_path):
    for file in files:
        print(file)  # Print each file name found