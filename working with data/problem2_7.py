#Problem 7: Python has built-in functions min and max to compute minimum and maximum of a given list. Provide an implementation for these functions. What happens when you call your min and max functions with a list of strings?

def min(lst):
 #assuming frst element is minimum
   minimum=lst[0]
   for item in lst[1:]:
        if item<minimum:
             minimum=item
   return minimum
        


def max(lst): #assuming frst element is maximum
   maximum=lst[0]
   for item in lst[1:]:
        if item>maximum:
             maximum=item
   return maximum
        

print (min(["apple","banana","cherry"]))
print (max(["apple","banana","cherry"]))
print (min([3,1,4,2]))
print (max([3,1,4,2]))

