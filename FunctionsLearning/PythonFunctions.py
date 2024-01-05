"""There are two type of functions
1. Build in function
2. User defined function
"""

"""Arguments in python
1. Default Argument"""
def properties(height, color="red"): #providing default value of color
    print("--------Default Argument--------")
    print("Hi I am Nitin and my height is {0} and my color is {1}".format(height,color))
properties(3, "Orange")

"""2. Keyword Argument"""
def properties1(height=3, color="black",myclass=7):
    print("--------Keyword Argument--------")
    print("Hi I am Nitin and my height is {0} and my color is {1}".format(height,color))
    print("I am in class {}".format(myclass))
properties1()

"""3. Position Argument"""
def properties2(height, color,myclass):
    print("--------Position Argument--------")
    print("Hi I am Nitin and my height is {0} and my color is {1}".format(height,color))
    print("I am in class {}".format(myclass))
properties2(2,"REd", 7)

"""3. Arbitrary Keyword Argument"""
def properties3(*argt): #Passing non-keyword Argumnet
    print("--------Non Keyword Arbitrary Argument--------")
    print(argt)
    for n in argt:
        if n == 24:
            print("{} is my number".format(n))
properties3(23,45,24,67)

def properties4(**kargs):
    print("--------Keyword Arbitrary Argument--------")
    for key, value in kargs.items():
        print("{} is {} years old".format(key,value))
properties4(Nitin=7,sachin=9,pooja=8)

"""args and kwargs both can be used as the argument of same function"""

def myFunction(*args, **kwargs):
    print("-----------Having args and kwargs both--------------")
    print("these are args", args)
    print("these are kwargs", kwargs)
myFunction("nitin","kulshreshtha",age=24, myclass="fifth")











