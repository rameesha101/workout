#Problem 3: What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.
 

def sum(items):
  result=items[0]
  for i in items[1:]:
     result+=i
     return result
  
 
  print(sum("hello","world"))

  print(sum([1,2,3,4]))