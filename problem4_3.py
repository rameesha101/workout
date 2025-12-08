#Problem 3: What will be the output of the following program?


try:
    print("a")
    raise Exception("doom")
except:
    print("b")
else:
    print("c")
finally:
    print("d")


#Answer: The output will be:
#a
#b
#d
#Explanation:a is printed first. Then an exception is raised, causing  the program to jump to the except block, printing b. The else block is skipped because an exception occurred. Finally, the finally block is executed, printing d.    