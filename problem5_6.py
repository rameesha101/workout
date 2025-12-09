#Problem 6: Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively

#Problem 5: Write a function to compute the total number of lines of code in all python files in the specified directory recursively.
import os

def findfiles(directory):                    #function to find files recursively
     for root, dirs, files in os.walk(directory):   #walk through the directory
         for file in files:
             for file in files:
                 yield os.path.join(root, file)   #yield the full path of the file

def count_py_files(directory):
     return sum(1 for file in findfiles(directory) if file.endswith('.py'))  #count .py files

#we wnt Count non-empty, non-comment lines in all Python files recursively.
def count_code_lines_in_py_files(directory):         
        total_lines = 0
        for file in findfiles(directory):
            if file.endswith('.py'):
                with open(file, 'r',errors="ignore") as f:      #open the .py file,also ignore encoding errors 
                        for line in f:
                            line = line.strip()
                        
                            if line and not line.startswith('#'):  #check for non-empty, non-comment lines
                                total_lines += 1
        return total_lines


#example


example_directory = "//wsl.localhost/Ubuntu-24.04/home/rameeshap/workouts"
print("Number of .py files:", count_py_files(example_directory))
print("Number of lines in .py files:",count_code_lines_in_py_files(example_directory))
