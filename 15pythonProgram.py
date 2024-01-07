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

"""Prime Numbers"""
def isItPrime(num):
    print("-------check if a number is prime--------")
    if num > 1:
        for i in range(2, int(num/2)+1):
            if num%i == 0:
                print("{} is not a prime number".format(num))
                break
        else:
            print("{} is a prime number".format(num))
    else:
        print("{} is not prime number".format(num))
isItPrime(5)

def printAllPrimeNo(start, end):
    print("----------print all prime number b/w required range------------")
    list = []
    for expNO in range(start,end + 1):
        if expNO == 0 or expNO == 1:
            continue
        for i in range(2, int(expNO/2)+1):
            if expNO%i == 0:
                break
        else:list.append(expNO)
    return list

print(printAllPrimeNo(1, 50))

"""List"""
def multiplyAllListno(list):
    print("-------print all no. in the list--------")
    ans = 1
    for i in list:
        ans = ans * i
    return ans
list_no = [10,4,6,3,2,9]
ans = multiplyAllListno(list_no)
print(ans)

def smallestNo(list):
    print("------print smallest number in the list---------")
    min = list[0]
    for i in list:
        if min > i:
            min = i
    print("smallest number in the list is:{}".format(min))
smallestNo(list_no)

def confirmNoInList(list, no):
    print("----to find if number is present in the list-----")
    for i in list:
        if i == no:
            print("{} is present in the list".format(no))
            break
    else:
        print("{} is not present in the list".format(no))
confirmNoInList(list_no, 7)

def isNumberOddOrEven(num):
    print("------confirm even or odd--------")
    if num%2 == 0:
        print("{} no is even".format(num))
    else:
        print("{} no is odd".format(num))
isNumberOddOrEven(8327492)







