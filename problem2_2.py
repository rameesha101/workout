#Problem 2: Python has a built-in function sum to find sum of all elements of a list. Provide an implementation for sum.


def sum(numbers):
    total=0
    for n in numbers:
      total+=n
    return total
print(sum([1,2,3]))