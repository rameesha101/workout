"""x = 1
def f():
        y = x
        x = 2
        return x + y
print(x)
print(f())
print(x)
this shows error due to not defining a local variable x.
This can be corrected adding a line 
global x

"""
x=1
def f():
    global x
    y=x
    x=2
    return x+y
print(x)
print(f())
print(x)

