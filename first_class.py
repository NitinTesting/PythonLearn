class myself:
    b = 2
    def printname(self,name):
        print(name)

p = myself()
p.printname("nitin")

class printname:
    def __init__(self,name):
        print(name)

obj = printname("nitin")
