#Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction.

class reverse_iter:             #define the iterator class
    def __init__(self, list):          #initialize with the list to be iterated
     self.list = list                    #store the list
     self.index = len(list)-1     #start from the last element
    
    
    def __iter__(self):
        return self      #return the iterator object itself
    
    def __next__(self):
        if self.index>=0:      #if there are elements left to iterate
            value = self.list[self.index]  #get the current element
            self.index -= 1
            return value        #return the current element
        else:
            raise StopIteration
    

#example
a=[1,2,3,4,5]
rev_iter = reverse_iter(a)
print(next(rev_iter))  #5
print(next(rev_iter))  #4
print(next(rev_iter))  #3
print(next(rev_iter))  #2
print(next(rev_iter))  #1
print(next(rev_iter))  #StopIteration  