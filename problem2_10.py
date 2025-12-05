#Problem 10: Write a function unique to find all the unique elements of a list.


def unique(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(unique([1,2,2,3,4,4,5,5,5]))
