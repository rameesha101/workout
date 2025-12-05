#Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.


def cum_product(lst):
    result = []
    total = 1
    for itm in lst:
        total *= itm
        result.append(total)
    return result

print(cum_product([1,2,3,4])) 


 # Output: [1, 2, 6, 24]