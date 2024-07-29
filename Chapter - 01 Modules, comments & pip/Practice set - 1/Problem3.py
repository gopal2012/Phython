#  Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that

import os

# Function to print the contents of a directory
def print_directory_contents(directory):
    try:
        # Get the list of files and directories
        contents = os.listdir(directory)
        
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory you want to list
directory_path = "/workspaces/Phython"  # Replace with the actual path

# Call the function to print the directory contents
print_directory_contents(directory_path)
