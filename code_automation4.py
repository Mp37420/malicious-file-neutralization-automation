import os
import re

# Program starts here
print("Searching for malicious files...")

# Define the IP address pattern to search for
ip_pattern = r"8\.13\.193\.9"  # Regular expression for exact match

# Start iterating over the files present in the clients_sites folder
complete_path = os.path.dirname(os.path.abspath(__file__))
for root, _, files in os.walk(complete_path + "/clients_sites"):
    for file in files:  # Iterate over the files in the directory
        file_path = os.path.join(root, file)
        malicious = False  # Flag to check if the file is malicious

        try:
            # Check if the file starts with 'xmc6_'
            if file.startswith('xmc6_'):
                print(f"Found malicious file by prefix: {file}")
                malicious = True

            # Open each file and check if it contains the IP address
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

                # Step 2: Check if the content contains the IP address using the regex
                if re.search(ip_pattern, content):
                    print(f"Found malicious file with IP: {file}")
                    malicious = True

        except Exception as e:
            # Handle any file reading errors (e.g., permission errors)
            print(f"Error reading file {file_path}: {e}")

        # If the file is identified as malicious, rename it by adding a .txt extension
        if malicious:
            print(f"Renaming file {file}")
            new_name = file + ".txt"
            new_file_path = os.path.join(root, new_name)
            os.rename(file_path, new_file_path)  # Renaming the file
            print(f"File renamed to: {new_name}")
    