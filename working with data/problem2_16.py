#Problem 16: Write a function extsort to sort a list of files based on extension.
# input:extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

def extsort(lst):
    return sorted(list, key=lambda x: (x.split('.')[-1], x))

print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))    


#output: ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']