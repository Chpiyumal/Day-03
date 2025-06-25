import os

#Define the directory you want to change to
#Make sure this directory exist in system
new_directory = "./tmp" # Example for Linux/macOS
# For Windows, it might be something like "C:\\Users\\..."

if os.path.exists(new_directory) and os.path.isdir(new_directory):
    os.chdir(new_directory)
    print(f"Changed Directory to : {os.getcwd()}")
else:
    print(f"Directory '{new_directory} does not exist or is not a directory")