def printMe(a,b,c=0): #exapmple of polymorphism :  function polymorph
    print(a+b+c)

printMe(4,5)
printMe(2,3,5)

"""Example of class polymorphism"""

class nitin:
    def name(self):
        print("Nitin")
    def income(self):
        print("100000")

class sachin:
    def name(self):
        print("sachin")
    def income(self):
        print("80000")

member1 = nitin()
member2 = sachin()

for x in (member1, member2):
    x.name()
    x.income()
