import os

# Start of the program
print("Searching for malicious files...")

# Get the absolute path of the current script
script_path = os.path.abspath(__file__)

# Get the directory where the script is located
script_dir = os.path.dirname(script_path)

# Define the path to the clients_sites folder
base_path = os.path.join(script_dir, "clients_sites")

# Traverse through all files in the clients_sites folder
for root, _, files in os.walk(base_path):
    for file in files:  
        if file.startswith("xmc6_"):  # Check if the file starts with 'xmc6_'
            print(file)  # Print the malicious file name

