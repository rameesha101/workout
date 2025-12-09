#Problem 1: Write a program to list all files in the given directory.


import os
def list_files(path):
    files=os.listdir(path)
    for file in files:
        print(file)

#example using current folder
print(list_files('.'))