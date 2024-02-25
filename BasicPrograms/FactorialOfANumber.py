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

