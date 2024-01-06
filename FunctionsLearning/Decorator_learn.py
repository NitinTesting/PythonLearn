"""Different usage of function"""
def loud(text):
    return text.upper()
def whisper(text):
    return text.lower()
s = loud("Hello") #function as an opject
print("-----function as a object ---------")
print(s)
def greatings(type, text):
    return (type(text))
s= greatings(loud,"Hello Everyone") #function as an object
print("-----function as a object ---------")
print(s)
def outer(a):
    def inner(b):
        return "value of outer is {} and inner is {}".format(a,b)
    return inner #function returning other function
outer_val = outer(5)
inner_val = outer_val(6)
print("-----function as a return value ---------")
print(inner_val)

"""Understanding what actually decorator will do"""
def hello_decorator(func):
    def wrapped_function():
        func() #here we can call any other function using decorator
        print("This will be print after other function is called")
    return wrapped_function

def function1():
    print("-----Functionality of a decorator function without using annotation---------")
    print("This will print other function 1")
function1 = hello_decorator(function1)
function1()

@hello_decorator
def function_to_be_called():
    print("-----Functionality of a decorator function using annotation---------")
    print("This will print other function 2")
function_to_be_called()

"""Decorators allow us to wrap another function in order to extend 
the behaviour of the wrapped function, without permanently modifying it"""
def decoroator1(func):
    def wrapper_func(*args): # Wrapped function whose behaviour will change as per other function using decorator
        func(*args)
    return wrapper_func

@decoroator1
def function1(*args):
    print("-------first function to extend the behaviour--------")
    for i in args:
        print(i)

@decoroator1
def function2(a, b):
    print("-------first function to extend the behaviour--------")
    print(a + b)

function1("Jhon", "Tony")
function2(3, 7)






