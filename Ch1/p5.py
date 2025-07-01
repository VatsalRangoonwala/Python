# Label the program written in problem 4 with comments.

import os  # Import the OS module to interact with the operating system

# Set the directory path ('.' refers to the current directory)
directory_path = "."

try:
    # Get the list of files and folders in the specified directory
    contents = os.listdir(directory_path)
    
    # Print the absolute path of the directory
    print(f"Contents of directory: {os.path.abspath(directory_path)}\n")
    
    # Print each item in the directory
    for item in contents:
        print(item)

# Handle case where the directory does not exist
except FileNotFoundError:
    print("The specified directory does not exist.")

# Handle case where permission is denied
except PermissionError:
    print("Permission denied to access the directory.")