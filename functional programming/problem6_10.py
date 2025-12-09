#Problem 10: Write a function profile, which takes a function as argument and returns a new function, which behaves exactly similar to the given function, except that it prints the time consumed in executing it.



import time    # for time measurement
def profile(func):         
    def wrapper(*args, **kwargs):         #args and kwargs to accept any number of arguments
        start_time = time.time()    #start time measurement       
        result = func(*args, **kwargs)                 #call the original function
        end_time = time.time()                       #end time measurement
        print(f"time taken: {end_time - start_time} sec")               #print time taken
        return result             #return the result of the original function
    return wrapper           #return the wrapper function

    #example:fibonacci function

    def fib(n):
        if n ==0 or n==1:
            return n
        else:
          return fib(n-1) + fib(n-2)

#wrapping fib with profile
fib = profile(fib)
print(fib(20))  #prints time taken and result of fib(20)


