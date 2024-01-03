#List example
family = ["Nitin", "Pooja", "Ishanvi", "Sachin"] # created using []
cast = ["kumar","Kulshreshtha"]
print(family[0])# this is how you can access the list items by index starting from 0
print(family[-1])# access the list items by index from end item
print(len(family)) # len() function will return the length of the list
for n in family:
    print(n,"kulshreshtha")
family.extend(cast) #extend will add another list to an list
print(family)
"""
list are used to store multiple values in a single variable
List Items are 
ordered - Items in the list have a defined order
changeable - we can remove, replace and add items in the list after creation
allow duplicate values - list can have duplicate values

Type of the List is 'list'
"""
#Items in the list can have any data type, and can have different data types
myDetails = ["Nitin", 36, "GrNo", "Pooja", 59, "Delta 1", "Ishanvi"]
print("My name is {0} and I am {1} years old".format(myDetails[0], myDetails[1]))
print(myDetails[2:5]) #return index no 2, 3, 4
print(myDetails[2:]) #return all values of and after index 2
print(myDetails[:5]) #return all values before index 5
if "Nitin" in family: #if item is present in a list
    print("Yes we have him")
else:
    print("No we dont")

"""Changing/replacing the items in the list"""
myDetails[6] = "Sachin" #replacing single item to another item via index
print(myDetails)
myDetails[6:7] = ["Ishanvi", "Sachin"] #replace a range of items to single, multiple items
print(myDetails)
myDetails.insert(2, "Greater Noida") #add another item in middle of the list
print(myDetails)
myDetails.append("Nisha") #add another item in the list at the end
print(myDetails)

"""Removing of the items in the list
can be done by remove, pop and del
remove() - Remove method will remove specified item
pop() - is a method to remove specific index
del  - is a keyword to remove specific index """

newList = ["Nitin", "Sachin", "pooja", "Ishanvi","Kuldeep", "Nisha", "Sachin"]
print(newList)
newList.remove("Sachin") # will remove specific item,
# if that item duplicates then only first item will get deleted
print(newList)
newList.pop(5) # will remove specific index.
# pop() will remove the last item by default if used without entering any index value
print(newList)
del newList[1] # keyword to remove any index value from the list
print(newList)


"""List Comprehension
It enable user to use shorter syntex to create a new list using an existing list"""

# new_list = [<expression> for <item> in <iterable> if <condition = true>]
new_list = [x for x in newList if "i" in x]
#create a new list of item from existing list which have 'i' as an character
print(new_list)
new_list1 = [x for x in newList] # with no if condition it will create exact copy of the existing one
print(new_list1)
new_list2 = [x.upper() for x in newList] #Crete a new list with some changes in the existing one
print(new_list2)
newList.clear() #method to empty the list
print(newList)
"""Sorting
sort() and sort(reverse = True) is used to sort the list ascending and descending orders respectively"""
numlist = [1, 56, 3, 90, 67]
alphlist = ["sachin", "Pooja", "Nitin", "Ishanvi"]
numlist.sort()
print(numlist)
alphlist.sort(reverse=True)
print(alphlist)
list1 = alphlist.copy() #will copy the list
print(list1)
# another way to copy is using list keyword
list2 = list(numlist)
print(list2)

"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list


"""
