#Problem 4: What will be the output of the following program?


def f():
    try:
        print("a")
        return
    except:
        print("b")
    else:
        print("c")
    finally:
        print("d")

f()


#Answer: The output of the program will be:
#a
#d
#Explanation:           
#When the function f() is called, it enters the try block and prints "a".
#Then, the return statement comes, causing the function to prepare to exit.finally block is executed before the function actually returns, so "d" is printed next.
#The except and else blocks are skipped because there was no exception and the function is returning.       