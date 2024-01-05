"""Global Variable : Defined outside any function
Local Variable : Defined inside any Function"""

a = "This is the Global Variable"
def printlocal():
    a = "This is the local Variable"
    print(a) # this will print the local variable
    """If a local variable is of same name of a global variable then it will create a new memory rather 
    than changing the value of existing one"""
def printglobal():
    print(a) # this will print the global variable
printlocal()
printglobal()
"""We can not change the value of any variable inside a function"""
def change():
    try:
        b = "{} : this is the change".format(a)
        a = b #trying to change the value of the global variable
        print(a)
    except UnboundLocalError:
        print("Error occurred when try to change the global variable")
"""We can change the value of any variable inside a function using Global Keyword"""
def change_using_global_keyword():
    try:
        global a
        b = "{} : this is the change".format(a)
        a = b #trying to change the value of the global variable
    except UnboundLocalError:
        print("Error occurred when try to change the global variable ")
change()
change_using_global_keyword()
print(a) #printing global variable after calling the function where its value is chaged

