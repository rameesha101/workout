#Problem 15: Reimplement the unique function implemented in the earlier examples using set

def unique(lst):
    return list(set(lst))
#since set fn is a unique collection of elements
  
print(unique([1, 2, 2, 3, 4, 4, 5]))  



# Output: [1, 2, 3, 4, 5]