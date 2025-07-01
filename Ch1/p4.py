# Write a python program to print the contents of a directory using the os module.

import os

directory_path = "."

try:
    contents = os.listdir(directory_path)
    
    print(f"Contents of directory: {os.path.abspath(directory_path)}\n")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("Permission denied to access the directory.")
