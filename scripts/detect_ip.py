import os
import re

# Searching for malicious files with the IP address 8.13.193.9
print("Searching for malicious files with IP address 8.13.193.9...")

# Pattern to search for the IP address in files
ip_pattern = r"8\.13\.193\.9"  # This is the exact IP pattern

# Walk through all files in the "clients_sites" folder
complete_path = os.path.dirname(os.path.abspath(__file__))  # Get the current folder
for root, _, files in os.walk(complete_path + "/clients_sites"):  # Iterate through all files
    for file in files:  # Check each file
        file_path = os.path.join(root, file)  # Get the full file path

        try:
            # Open the file and read its content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

                # If the IP address is found in the content, it's malicious
                if re.search(ip_pattern, content):  # Search for the IP
                    print(f"Malicious file found (RegEx): {file}")  # Print the file name
                    print(f"File content preview: {content[:500]}")  # Show a preview of the content

                    # Rename the file by adding ".txt" at the end
                    new_name = file + ".txt"
                    new_file_path = os.path.join(root, new_name)  # Get the new file path
                    os.rename(file_path, new_file_path)  # Rename the file
                    print(f"File renamed to: {new_name}")  # Print confirmation

        except Exception as e:
            # If there’s an error reading the file (e.g., it's being used by another process)
            print(f"Error reading file {file_path}: {e}")
