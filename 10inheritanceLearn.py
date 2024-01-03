class family:  # Parent Class
    father = "Kuldeep"
    mother = "Nisha"
    __myself = "titanic"
    def __init__(self, name): # parent Class constructor
        self.name = name
    def display(self):
        print(self.name)
        print(self.__myself)
class child(family): # child class inheriting parent class
    child1 = "Sachin"
    child2 = "Nitin"
    def __init__(self, age, name): #constructor of the child class
        self.age = age
        family.__init__(self,name) # invoking the constructor of parent class with child class constructor

class child1(child):
    def __init__(self,name1,name):
        self.name1 = name1
        super().__init__(self,name) # Super function returns the object that represent the parent class

    def info(self):
        print(self.name1)

obj = child(3, "F331")
print(obj.father)
obj.display()

obj1 = child1("nitin", "sachin")
obj1.display()

"""multiple inheritance"""

class father:
    def __init__(self,fathername, fatherage):
        self.fathername = fathername
        self.fatherage = fatherage
class mother:
    def __init__(self,mothername,motherage):
        self.mothername = mothername
        self.motherage = motherage
class family(father, mother): # multiple inheritance
    def __init__(self,fname,fage,mname,mage):
        father.__init__(self,fname,fage)
        mother.__init__(self,mname,mage)

obj = family("Nitin", 36, "Pooja", 32)
print(obj.fathername)
print(obj.motherage)

