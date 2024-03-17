# Python program to demonstrate
# implicit type Casting

# Python automatically converts
# a to int
a = 7
print(type(a))

# Python automatically converts
# b to float
b = 3.0
print(type(b))

# Python automatically converts
# c to float as it is a float addition
c = a + b
print(c)
print(type(c))

# Python automatically converts
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))


# Python Convert Int to Float

num = 7

num1 = float(7)

print(num1)
print(type(num1))

# Python Convert Float to Int

num = 5.66

num1 = int(num)
print(num1)
print(type(num1))

#Python Convert int to String

num = 789

string = str(num)
print(string)
print(type(string))

# Python Convert String to float

a = "5.88"
floatt = float(a)
print(floatt)
print(type(floatt))

# string variable
a = "5"
b = 't'

# typecast to int
n = int(a)

print(n)
print(type(n))

# print(int(b))
# print(type(b))

# -------
# ValueError                                Traceback (most recent call last)
# Cell In[3], line 14
#      11 print(n)
#      12 print(type(n))
# ---> 14 print(int(b))
#      15 print(type(b))
#
# ValueError: invalid literal for int() with base 10: 't'

# Addition of string and integer Using Explicit Conversion
# integer variable
a = 5
# string variable
b = 't'

# typecast to int
# n = a+b

# print(n)
# print(type(n))

# TypeError                                 Traceback (most recent call last)
# Cell In[5], line 10
#       7 b = 't'
#       9 # typecast to int
# ---> 10 n = a+b
#      12 print(n)
#      13 print(type(n))


