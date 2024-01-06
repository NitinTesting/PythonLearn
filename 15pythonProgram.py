"""Fibonacci Sereies"""
def fibonacciNo(num):
    print("-------fibonacci series using yield----------")
    a = 0
    b = 1
    for i in range(num):
        yield a
        a , b = b, a+b

fibonacciSeries = fibonacciNo(10)
for i in fibonacciSeries:
    print(i)
def fibonacciNo1(num):
    print("------fibonacci series using for--------")
    a = 0
    b = 1
    for i in range(num):
        print(a)
        a , b = b, a+b
fibonacciNo1(10)

"""Factorial NUmber"""
def factno(num):
    print("---------factorialNo-------")
    fact = 1
    while num >= 1:
        fact = fact * num
        num = num - 1
    print(fact)
factno(3)

"""reversing a list or a string"""
def reverseString(myString):
    print("----------reverse string-----------")
    print(myString[::-1])#starts at the end move to 0 with -1 step
reverseString("I am here")

def reverseAList(list):
    print("----------reverse list-----------")
    print(list[::-1])
a = [1,4,5,6,32,2]
reverseAList(a)

"""Swapping a number"""
def swapNum(a , b):
    print("-------numbers before swapping--------")
    print("value of a is {}".format(a))
    print("value of b is {}".format(b))
    print("-------numbers after swapping--------")
    a , b = b, a
    print("value of a is {}".format(a))
    print("value of b is {}".format(b))

swapNum(3, 4)

"""Finding Largest number"""
def findLargestNumber_forLoop(list):
    print("-----largest number using for loop----")
    max = list[0]
    for i in (list):
        if i > max:
            max = i
    print("largest number is :{}".format(max))

def findLargestNumber_sort(list):
    print("-----largest number using sort----")
    list.sort()
    print(list[-1])
a = [1,4,55,6,32,2]
findLargestNumber_forLoop(a)
findLargestNumber_sort(a)
