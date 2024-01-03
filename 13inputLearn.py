from configparser import ConfigParser
a = input("write your name -") #will take an input after the mentioned caption and save it in a
b = input("write your title -")
print("hello {0} {1}".format(b,a))
config = ConfigParser() #obj is needed to parse through config file
config.read("./project_resources/config.cfg")
username = config.get("Section1","username")
print(username)