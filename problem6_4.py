"""Problem 4: Write a function treemap to map a function over nested list.

treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]"""

def treemap(func, nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):    #if it is a list, go deeper
            result.append(treemap(func, item))
        else:                                   #if it is not a list, apply the function
            result.append(func(item))
    return result


print(treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]))  
