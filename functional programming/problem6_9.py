"""Problem 9: Write a function permute to compute all possible permutations of elements of a given list.
permute([1, 2, 3])
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]"""


def permute(lst):
    #if 1 element ,only 1 permutation
    if len(lst) <= 1:
        return [lst]
    
    ans=[]

    for i in range(len(lst)):
        first = lst[i]
        rest = lst[:i] + lst[i+1:]   #remove selected element

        for p in permute(rest):
            ans.append([first] + p)  #add selected element to front of each permutation of rest

    return ans

print(permute([1, 2, 3]))
