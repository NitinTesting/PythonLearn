#tupple example
family = ("Nitin", "Pooja", "Ishanvi", "Sachin") # created using ()
cast = ("kumar","Kulshreshtha")
print(family[0])# this is how you can access the tupple items by index starting from 0
print(family[-1])# access the tupple items by index from end item
print(len(family)) # len() function will return the length of the tupple

"""
Tupple are use to store multiple items in a single variable
Tupple Items are 
ordered - Items in the list have a defined order
Unchangeable - we can not remove, replace and add items in the list after creation
allow duplicate values - list can have duplicate values
datatype of tupple is 'tupple'
"""
myDetails = ("Nitin", 36, "GrNo", "Pooja", 59, "Delta 1", "Ishanvi")
print("My name is {0} and I am {1} years old".format(myDetails[0], myDetails[1]))
print(myDetails[2:5]) #return index no 2, 3, 4
print(myDetails[2:]) #return all values of and after index 2
print(myDetails[:5]) #return all values before index 5

"""
We can not change/update/add a tupple but there is a workaround
change the tupple to a list using type casting
update the list and then again change the list to a tupple using type casting
"""

castlist = list(cast)
print(type(castlist))
castlist.append("tata")
cast = tuple(castlist)
print(type(cast))
print(cast)

"""Unpacking a tupple
extracting the values from the tupple and assigning them with variables
"""
(head, wife, daughter, brother) = family
print(brother)


"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

"""
