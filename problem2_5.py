
#Problem 5: Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?

def product(numbers):
    result=1
    for n in numbers:
        result*=n
    return result

#now using product function we write factorial function

def factorial(n):
    return product(range(1,n+1))

print("factorial of 4 is:",factorial(4))
