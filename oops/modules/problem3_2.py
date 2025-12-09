#Problem 2: Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.


import os

def extcount(folder):
    counts = {}   # empty dictionary

    for name in os.listdir(folder):   # look at each file
        if "." in name:               # check if it has an extension
            ext = name.split(".")[-1]   # get extension
        else:
            ext = "no_extension"

        # if extension not seen before, start with 0
        if ext not in counts:
            counts[ext] = 0

        # add 1 to that extension count
        counts[ext] += 1

    # print results
    for ext in counts:
        print(ext, counts[ext])

# example:
print(extcount("."))   # "."  current folder


"""output
py 53
txt 2
no_extension 2
git 1
md 1
None"""