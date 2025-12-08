#Problem 13: Write a function lensort(list) that takes a list of strings and returns a list sorted by the length of the strings.

def lensort(list):
    return sorted(list, key=len)

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])) 


 # Output: ['c', 'perl', 'java', 'ruby', 'python', 'haskell']