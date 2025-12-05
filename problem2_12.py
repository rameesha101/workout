#Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.


def group(list, size):
    result=[]
    for i in range(0, len(list), size):
        result.append(list[i:i+size])
    return result
    
print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) 


 # the Output is: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]