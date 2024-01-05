"""Yield allows to produce a series of values over time, rather than
computing them at once and sending them back as a list like return"""
def simple_yield_funciton(num): #Generator Function -
    # A generator function in Python is defined like a normal function,
    # but whenever it needs to generate a value,
    # it does so with the yield keyword rather than return
    i = 1
    for n in range(10): #a loop to generate some values
        yield i*num #will generate again and again till loop ends
        i += 1

"""This is how we can generate all values at one go"""
print("---------Printing all values on one go--------------")
genObj = simple_yield_funciton(8) #Generator_Object -
# generator object that is iterable, i.e., can be used as an Iterator

for value in genObj:
    print(value) #printing generated value using for loop

"""This is how we can generate values one by one"""
b = simple_yield_funciton(3)
print("---------Printing values one by one--------------")
print(next(b)) #Print first generated value on first call
print(next(b)) #print next generated value and so on.....
print(next(b))

"""Return sends a specified value back to its caller whereas Yield can produce a 
sequence of values. We should use yield when we want to iterate over a sequence, 
but don’t want to store the entire sequence in memory. """


"""Fibonacci series"""
def creatFibonacci(num):
    a = 0
    b = 1
    for n in range(num):
        yield a
        a , b = b , b + a

value = creatFibonacci(5)
print("----------print Fibonacci Series-----------")
for n in value:
    print(n)

