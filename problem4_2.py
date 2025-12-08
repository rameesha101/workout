#Problem 2: What will be the output of the following program?
try:
    print("a")
except Exception as e:
    print("b")
else:
    print("c")
finally:
    print("d")


#the output will be:
             #a
             #c
             #d  
#Explanation:
#The try block executes successfully and prints "a". Since there is no exception, the else block is executed next, printing "c". Finally, the finally block is executed, printing "d".