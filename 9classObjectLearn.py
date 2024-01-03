class family:  # this is how a class is defined by class keyword
    father = "Kuldeep"  # these are the variables which can be used as the attributes of the class
    myselfe = "Nitin"

    def __init__(self, name):

        if name == "father":
            print(self.father)
        else:
            print(self.myselfe)


fam = family("father")  # this is how we create an object of the class to use the attributes of the class
print(fam.__class__.myselfe)


class hello:
    def __init__(self,name):
        self.name = name

    def sayHi(self):
        print("hi i am {}".format(self.name))

obj = hello("Nitin")
obj.sayHi()


class animal: # using self is not mandatory, we can use anything it just have to be the first parameter
    def __init__(pagal, name):
        pagal.name = name
    def whoyouare(chor):
        print(chor.name)

obj = animal("tiger")
obj.whoyouare()

class details:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  #You can alter how objects of a class are represented in strings by defining the __str__() method
        return "my name is {0}, and my age is {1}".format(self.name, self.age)

myDetails = details("Nitin", 36)
print(myDetails)


