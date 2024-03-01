try:
   x = int(input("enter a number"))
   print(x)
except:
    print('number is not an integer')


#

try:
    x = int(input("enter a number"))
    print(x)
except ValueError:
    print('number is not an integer')

    #

try:
    x = int(input("enter a number"))
    print(x)
except ValueError:
    print('number is not an integer')
finally:
    print('is in finally block')

# catching specific exception
# The code defines a function ‘fun(a)' that calculates b based on the input a.
# If a is less than 4, it attempts a division by zero, causing a ‘ZeroDivisionError'.
# The code calls fun(3) and fun(5) inside a try-except block.
# It handles the ZeroDivisionError for fun(3) and prints “ZeroDivisionError Occurred and Handled.”
# The ‘NameError' block is not executed since there are no ‘NameError' exceptions in the code.
def fun(a):
    if a < 4:

        b = a/(a-3)
    print("Value of b = ", b)

try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

#

def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print(c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#
try:
    k = 5//0
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')


#

try:
    raise NameError("Hi there")
except NameError:
    print ("An exception")
    raise

