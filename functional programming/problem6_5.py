"""
Problem 5: Write a function tree_reverse to reverse elements of a nested-list recursively.

tree_reverse([[1, 2], [3, [4, 5]], 6])
[6, [[5, 4], 3], [2, 1]]"""

def tree_reverse(nested_list):
   result = []
#reverse the list first
   for item in reversed(nested_list):    #if item is a list, call tree_reverse recursively
       if isinstance(item, list):
           result.append(tree_reverse(item))
       else:            #otherwise, just append the item
           result.append(item)
           
   return result


print(tree_reverse([[1, 2], [3, [4, 5]], 6])) 


 # Output: [6, [[5, 4], 3], [2, 1]]
