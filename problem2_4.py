#Problem 4: Implement a function product, to compute product of a list of numbers.

def product(numbers):
    result=1
    for n in numbers:
        result*=n
    return result
print("product of [1,2,3,4] is:",product([1,2,3,4]))


#output :product of [1,2,3,4] is: 24
