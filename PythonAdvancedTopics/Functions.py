# simple built in function
def fun():
    return "inside function"


# Driver code to call a function
print(fun())


# add two numbers

def add(x: int, y: int) -> int:
    """Add two numbers"""
    z = x + y
    return z


x, y = 5, 7
z = add(x, y)
print(f"The addition of {x} and {y} results {z}.")

# Default Arguments

def myDef(x, y = 20):
    return x+y

print(myDef(10))

def myFullName(firstName, lastName ):
    return firstName+lastName

print(myFullName(firstName= "hello", lastName= " world"))
print(myFullName(lastName= " world", firstName= "hello"))

#Positional Arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

# You will get correct output because
# argument is given in order
print("Case-1:")
nameAge("Suraj", 27)
# You will get incorrect output because
# argument is not in order
print("\nCase-2:")
nameAge(27, "Suraj")

# *args
def myFun(*args):
    for i in args:
        print(i)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# **kargs

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s: , %s " % (key, value))

myFun(first='Geeks', mid='for', last='Geeks')

#Docstring

# A simple Python function to check
# whether x is even or odd

def evenOdd(x):
    """Function to check if the number is even or odd"""

    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
print(evenOdd.__doc__)

#Function within Functions

# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
    s = 'I love GeeksforGeeks'

    def f2():
        print(s)

    f2()

# Driver's code
f1()

# Anonymous Functions in Python

# Python code to illustrate the cube of a number
# using lambda function
def cube(x):
    return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))

# Recursive Functions
def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)

print(factorial(4))

# Return Statement in Python Function

def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2


print(square_value(2))
print(square_value(-4))


# Pass by Reference and Pass by Value
# Driver Code (Note that lst is modified
# after function call.

# Here x is a new reference to same list lst
def myFun(lst):
    lst[0] = 20

lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


def myFun(x):

    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = [20, 30, 40]


# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

#
def myFun(x):

    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = 20


# Driver Code (Note that x is not modified
# after function call.
x = 10
myFun(x)
print(x)

#Try to guess the output of the following cod

def swap(x, y):
    temp = x
    x = y
    y = temp


# Driver code
x = 2
y = 3
swap(x, y)
print(x)
print(y)


