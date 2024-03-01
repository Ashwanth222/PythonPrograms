# default value

# Python program to demonstrate
# default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


# Driver code (We call myFun() with only
# argument)
myFun(10)

#

# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')


#
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


#

# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# nested functions

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


# Recursive Functions in Python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))


# return statement

def squareOfANumber(num):
    return num**2

print(squareOfANumber(2))
print(squareOfANumber(-4))

# Pass by Reference and Pass by Value

def myFunction(x):
    x[0] = 34

y = [30, 40, 50, 60, 70, 80]
myFunction(y)
print(y)

# When we pass a reference and change the received reference to something else,
# the connection between the passed and received parameters is broken.
# For example, consider the below program as follows:

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


# Another example demonstrates that the reference link
# is broken if we assign a new value (inside the function).
# Driver Code (Note that x is not modified
# after function call.
x = 10
myFun(x)
print(x)

#
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


