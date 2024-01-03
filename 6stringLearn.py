a = "I am Nitin" #assiging a string to a variable
gender, name = a.split("am ")
print(a.upper()) #upper will return string in upper case,
b = """I live in delhi
with my daughter and wife
they are my life""" # assigning multiline string to a variable
print(b)
#String in python are arrays of bytes representing unicode character
for n in a:
    print(n.lower())#lower will return string in lower case
print(a[6])
print(len(a))
assert "daughter" in b, "not present in b" #checking substinrg in a string
print(a[6:9])#slicing of the string
print(a[6:])#slicing from end
print(a[:6])#slicing from start
print(a.strip())#strip() removes any white space from begining and the end
c = a.replace("Nitin", "Sachin")
print(c)
gender1, name1 = c.split("am ") # split will split a string into two substring
print(name1)
print(name,name1)
print(name + name1)
age = 6
print("my original name is {0} and age is {1}".format(name, age)) #.format will insert
# To insert characters that are illegal in a string, use an escape character.
# Eg: \' for	Single Quote
#     \n for New Line
