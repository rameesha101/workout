#Problem 5: Write a function to compute the total number of lines of code in all python files in the specified directory recursively.
import os

def findfiles(directory):                    #function to find files recursively
     for root, dirs, files in os.walk(directory):   #walk through the directory
         for file in files:
             for file in files:
                 yield os.path.join(root, file)   #yield the full path of the file

def count_py_files(directory):
     return sum(1 for file in findfiles(directory) if file.endswith('.py'))  #count .py files


def count_lines_in_py_files(directory):         
     total_lines = 0
     for file in findfiles(directory):
         if file.endswith('.py'):
             with open(file, 'r',errors="ignore") as f:      #open the .py file,also ignore encoding errors 
                 total_lines += sum(1 for line in f)  #count lines in each .py file
     return total_lines


#example


example_directory = "//wsl.localhost/Ubuntu-24.04/home/rameeshap/workouts"
print("Number of .py files:", count_py_files(example_directory))
print("Number of lines in .py files:",count_lines_in_py_files(example_directory))