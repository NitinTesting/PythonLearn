try:
    input1 = input("enter first number")
    input2 = input("enter second number")
    ans = int(input1) / int(input2)
    print(ans)

except ValueError:
    print("enter valied value")

except ZeroDivisionError:
    print("can not divide by zero")

finally:
    print("thanks for using me")


