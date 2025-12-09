#Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.

import os

def findfiles(directory):                    #function to find files recursively
     for root, dirs, files in os.walk(directory):   #walk through the directory
         for file in files:
             for file in files:
                 yield os.path.join(root, file)   #yield the full path of the file

def count_py_files(directory):
     return sum(1 for file in findfiles(directory) if file.endswith('.py'))  #count .py files

#example

example_directory = "//wsl.localhost/Ubuntu-24.04/home/rameeshap/workouts"

print("Number of .py files:", count_py_files(example_directory))