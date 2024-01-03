import random

def function1(name):
    print("this is how a function is created and its me {}".format(name))

function1("Nitin") # calling a function, we have to pass correct number of arguments

"""
Arbitrary arguments :
If we do not know that how many arguments will be passed then we can use *
this way function will receive a tupple of arguments items can be accessed acordinglly
"""

def family(*members):
    for n in members:
        print(n)

family("Nitin", "sachin", "pooja", "Nisha")

def myLuckyno(number):
    no = random.randint(1,10)
    no = no * number
    return no # this is how a function return a value

luckyNo = myLuckyno(5) # using the value returned by the function
print("my lucky no is: {}".format(luckyNo))

"""function as an argument of other function"""
def loud(text):
    return text.upper()
def whisper(text):
    return text.lower()
#function used as an object
say = loud("Hello") #object of the function
print(say)
def greetings(type):
    greetings = type("Hello Everone")
    print(greetings)
greetings(loud) #using function as an argument of the other function
greetings(whisper)

"""Function can return other function"""
def outer(x):
    def inner(y):
        return ("value of x is {0} and y is {1}".format(x,y))
    return inner #function is returning other function
first = outer("10")
second = first("12")

print(second)