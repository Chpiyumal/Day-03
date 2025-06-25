import os

path_to_check_file = "C:/Users/Student_15/Desktop/Python Chp/Codes/Day 03/tmp/my_existing_file.txt"
path_to_check_dir = "C:/Users/Student_15/Desktop/Python Chp/Codes/Day 03"

#Create a dummy for demonstration
with open(path_to_check_file, 'w') as f:
    f.write("Hello")
os.makedirs(path_to_check_dir, exist_ok=True)
