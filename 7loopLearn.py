"""
python has two primitive loop commands i.e.
1. while - will execute a set of code as long as condition is true
2. for - is used to iterate over a sequence i.e. a set, tupple, list or a dictionary
"""

i = 1
while i < 3: # condition is checked
    print(i) # set of code which run every time when condition is true
    i += 1
else:
    print("{} is the value".format(i)) # code run on else when condition is true and exection comes out of the loop

"""continue : stop current iteration and start next
break : stop all iteration even if the condition and upcoming conditions are true"""
def runLoop(number):
    i = 1
    while i < number:
        i += 1
        if i == 3:
            continue
        print(i)
runLoop(8)


name = "nitin" # used iterator as string
for n in name:
    print("character : {}".format(n))

iterator1 = ["Apple", "banana", "orange"] # used iterator as a list
for fruit in iterator1:
    if fruit == "banana":
        continue
    print(fruit)


"""range function : will give a sequence of number starting from 0 and increment by 1 by default 
and ends at specified number"""

for x in range(3): # will give 0, 1 and 2 in sequence, does not include 3
    print(x)

for x in range(2,6): # will give a range of 2 to 5 i.e. 2,3,4,5 excluding 6
    print("number is {}".format(x))

for x in range(2,14,2): # third parameter in the range update the increment value which is by default 1
    print(x)



