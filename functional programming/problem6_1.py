#Problem 1: Implement a function product to multiply 2 numbers recursively using + and - operators only


def product(a,b):
    # Base case (anything multiplied by 0 is 0 )
    if b == 0:
        return 0          
    
    if b < 0:
        return -product(a, -b)      # if b is negative, subtract the product of a and -b
    else:
        return a + product(a, b - 1)       #if b is positive, add a to the product of a and b-1
    

#example

print(product(5, 3))  # Output: 15
print(product(4, -2)) # Output: -8 
print(product(-3, 3)) # Output: -9
    