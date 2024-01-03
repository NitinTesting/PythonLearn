class whoAmI:
    def __init__(self):
        self.name = "ishu"
        print(self.name)

    def __str__(self):
        return "My name is :{}".format(self.name)

obj = whoAmI()
print(obj)




class localcall():

    def __int__(self1):
        self1.name = "sachin"

    def printnewname(self1):
        print(self1.name)

obj = localcall()
obj.printnewname()




