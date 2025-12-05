#Problem 13: Write a function lensort to sort a list of strings based on length.
'python', 'perl', 'java', 'c', 'haskell', 'ruby'])
['c', 'perl', 'java', 'ruby', 'python', 'haskell']

def lensort(list):
    return sorted(list, key=len)

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])) 


 # Output: ['c', 'perl', 'java', 'ruby', 'python', 'haskell']