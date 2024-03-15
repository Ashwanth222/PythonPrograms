# num = 18
# To take input from the user
num = int(input("Enter a number: "))
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


# alternate

# some more functions
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))