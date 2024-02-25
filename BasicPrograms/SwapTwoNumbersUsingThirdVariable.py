a = 5
b = 7
temp = 0
temp = a
a = b
b = temp
print("a",a)
print("b",b)
print('The value of a after swapping: {}'.format(a))
print('The value of b after swapping: {}'.format(b))

#Without temporary variable
x = 8
y = 9
x, y = y, x
print("x", x)
print("y", y)

#swapping using Addition and subtraction

k = 4
l = 7
k = k+l
l = k-l
k = k-l
print(k)
print(l)

#swapping using multiplication and division

e = 8
f = 4
e = e*f
f = e/4
e = e/8
print("e",e)
print("f",f)

#XOR swap

h = 2
i = 4

print("before xor operation h and i are",i,h)
h = h^i
i = i^h
print("after swapping i value is",i)
h = h^i
print("after swapping h value is",h)









