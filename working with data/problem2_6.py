#Problem 6: Write a function reverse to reverse a list. Can you do this without using list slicing?

def reverse(lst):
  result=[]
  for i in range (len (lst)-1,-1,-1):
        result.append(lst[i]) 
        return result
        print(reverse([1,2,3,4]))
          #then output will be :[4, 3, 2, 1] )
