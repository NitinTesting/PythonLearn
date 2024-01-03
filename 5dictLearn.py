family = {
    "myself": "Nitin",
    "wife": "Pooja",
    "age" : 34
} #dictionaries are written in {}
print(family)


"""
Dictionaries are used to store data in key-value pairs
Dictionaries are ordered, changeable and does not allow duplicates
data type of the dictionary is 'dict'
"""
print(family["wife"])
myAge = family["age"] #we have another method which give same result i.e. get()
wife = family.get("wife")
print("my age is {0} and wife name is {1}".format(myAge, wife))

print(family.keys()) #return the list of all keys
print(family.values()) #return the list of all values
print(family.items()) #return the list of all key-value pairs

if "wife" in family: #check if key is present in the dictionary
    print(family["wife"])

"""Updating the value of any key"""
family["age"] = 24
print(family)

family.update({"age": 33})
print(family)

"""We can use above two method to adding a new key-value pairs in dict"""
family["brother"] = "Sachin"
print(family)

family.update({"daughter" : "Ishanvi"})
print(family)

"""Removing the items in the dict"""
family.pop("brother") #method to delete the item with specific key
print(family)
del family["age"] #keyword to delete an item with specific key
print(family)
family.clear() #make the dict empty
print(family)
del family #delete the dictionary. if we print it now or try to access it, throws error

"""Creating the copy of a dictionary"""
opdict = {"son":"nitin", "wife":"Nisha" }
copydict = opdict.copy() #copy() method can be used to copy dictionary
copydict.update({"himself":"kuldeep"})
print(copydict)

copy2idct = dict(copydict) #build-in-function dict() can be used to copy dictionary
print(copy2idct)


"""
====Nested Dictionary===
A dictionary can contain multiple dictionaries, that dictionary is called nested dictionary 
"""
child1 = {"name":"Nitin",
          "age":36}
child2 = {"name":"Sachin",
          "age":32}
child3 = {"name":"Ishanvi",
          "age":5}
children = {"child1":child1,
            "child2":child2,
            "child3":child3}  # key has a value as dictionary and hence a single dict can have multiple dict

print(children["child2"])
print(children["child1"]["name"])


"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""