num = 5
factorial = 1
if(num == 1):
    print(1, "is a factorial of ", num)
elif(num == 0):
    print(1, "is a factorial of ", num)
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print(factorial)

#alternate
def factorial(num):
    if num == 1 :
        return 1;
    else:
        return (num*factorial(num-1))


num = 3
print("The factorial of", num, "is", factorial(num))


