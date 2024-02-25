num1 = 34
num2 = 35
if(num1 % 2) == 0:
    print(num1, "is even")
else:
    print(num1, "is odd")

if(num2 % 2) != 0:
    # print(num2, "is even")
    print("{0} is a odd number".format(num2))
else:
    print("{0} is a even number".format(num2))