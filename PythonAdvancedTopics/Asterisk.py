# Multiplication :

num1, num2 = 5, 6
mul = num1 * num2
print(mul)

# Exponentiation :

a = 6
b = 5
exp = 2 ** 5
print(exp)

# Multiplication of a list :
li = ['hello'] * 3
print(li)

# Unpacking a function using positional argument.

arr = ['sunday', 'monday', 'tuesday', 'wednesday']
print(" ".join(map(str, arr)))

print(*arr)

# Passing a Function Using with an arbitrary number of positional arguments

def summ(*args):
    return sum(*args)

print(summ([2,4,6,8,3,5,7]))

# Passing a  Function Using with an arbitrary number of keyword arguments

def fruits(**kwargs):
    for items in kwargs:
        print(f"{kwargs[items]} is a {items}")

fruits(name = "name1",age = 23,salary = 352532)

#
# using asterisk
def food(**kwargs):
    for items in kwargs:
        print(f"{kwargs[items]} is a {items}")

#

dict = {'fruit' : 'cherry', 'vegetable' : 'potato', 'boy' : 'srikrishna'}
# using asterisk
food(**dict)









