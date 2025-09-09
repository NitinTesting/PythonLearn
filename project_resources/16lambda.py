"""Lambda function
Lambda function are anonymous function that are created without a name, we dont have to use def
to create a function. we can use lambda to define it
syntex = lambda argument : expression
"""
a = lambda x: "findelement" if x == "single" else "findelements"
print(a("single"))
print(a("multiple"))

# function to create a list using lambda function
a = [lambda es=x: 2 * es for x in range(1, 11)]
for i in a:
    print(i())

# lamda function returning multiple results
x = lambda a, b: [a + b, "above" if a + b > 10 else "below"]

m = lambda c: [c * d for d in range(1, 11)]
print(m(2))

"""filter() function
filter() function takes function and a list as argument, used to filter those values for which
function returns true"""
a = ["nitin","pooja","sachin","nisha","kuldeep"]
mylist = filter(lambda x: "ni" in x,a)
print(list(mylist))

"""map() function
map() function takes function and list as argument, used to change all items in the list as per
the function"""

myfam = map(lambda x : x + " Kulshreshtha",a)
print(list(myfam))

