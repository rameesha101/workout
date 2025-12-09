#Problem 2: Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.

def long_lines(filenames):                 #define a generator function
    for f in filenames:
        for line in open(f):
            if len(line) > 40:           #check line length
                yield line

#main function to call the generator and print the lines
def main(filenames):
    for line in long_lines(filenames):
        print(line, end='')        #print the long lines without extra newlines



#running the program with an exmple file   sample.txt
main(['sample.txt'])
