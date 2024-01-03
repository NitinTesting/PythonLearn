
"""to read, write or update any text file we need to create and obj of the file
which will have two parameter, first will be the location and second is mode in
which you want to open it i.e. r:read, w:write, a:append,r+:read and write
"""
import os

obj = open("project_resources/jsonread.json", "r") #object of the file
print(obj.read()) # will read everything in the file

s = obj.readline() # will read the first line
while s:
     if "2" in s:
         print(s)
     s = obj.readline() #will read the all lines now

obj1 = open("./project_resources/valuesread1.txt", "w") #object of the file in write mode
obj1.write("This is new file 2")
os.remove("./project_resources/valuesread1.txt")


