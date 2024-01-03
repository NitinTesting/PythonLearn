family = {"Nitin", "Sachin", "Nisha", "Ishanvi"} # created using {}
print(family)
"""
sets are use to store multiple items in a single variable
sets Items are 
Unordered - Items in the sets do not have a defined order as they are unindexed
Unchangeable - we can not change items in the set after creation
But items can be added and removed from the set
Do not allow duplicate values in sets
datatype of sets is 'set'
"""
family1 = {"Pooja", "Nidhi", "Nidhi"} # duplicate values are ignored
print(family1)

"""access items in set"""

for n in family:
    print(n)

if "Nitin" in family:
    print("this is my family")

family.add("Kuldeep") #adding any item in the set
print(family)
family.update(family1) #adding any iterable eg.list,tupple or set to a set
print(family)

"""We can remove item using
remove() - keyword will remove the item and if item is not there will raise an error
discard() - keyword will remove the item and if item is not there will not raise an error
pop() - will remove any random item in the set as the items are not indexed
"""
family.remove("Nidhi")
print(family)
family.clear() #keyword to empty the set
print(family)
# del family #method to delete the set entirely
# print(family)

"""Joining Two Sets"""
a = {"Nitin", "Sachin", "Pooja"}
b = {"Sachin", 1, 23}
c = {"Nitin", 1, "Pooja"}
"""update and union will will join two set
update will update the existing set adding set
union will return a new set with both added sets
"""
a.update(b)
print(a)
d = b.union(c)
print(d)

"""Keeping only duplicate item from two set
intersection_update - will update the existing one
intersection - will return a new one with duplicates from both set
"""
a = {12, 34, 8, 43}
b = {34, 18, 19, 20}
c = {19 , 34, 20, 64}

a.intersection_update(b)
print(a)
d = b.intersection(c)
print(d)

"""Keeping only non duplicate item from two set
symmetric_difference_update - will update the existing one
symmetric_difference - will return a new one with duplicates from both set
"""
a = {12, 34, 8, 43}
b = {34, 18, 19, 20}
c = {19 , 34, 20, 64}

a.symmetric_difference_update(b)
print(a)
d = b.symmetric_difference(c)
print(d)

"""
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others

"""