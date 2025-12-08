#Problem 3: Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

import os

def findfiles(directory):       #function to find files recursively
    for root, dirs, files in os.walk(directory):   #walk through the directory
        for file in files:        #for each file in the files list
            yield os.path.join(root, file)   #yield the full path of the file

#Example
#for filepath  of  this workouts directory
for filepath in findfiles("//wsl.localhost/Ubuntu-24.04/home/rameeshap/workouts"):
    print(filepath)
