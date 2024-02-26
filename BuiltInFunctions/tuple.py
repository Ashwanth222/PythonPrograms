from itertools import count

t1 = tuple()
print('t1 =', t1)

# creating a tuple from a list
t2 = tuple([1, 4, 6])
print('t2 =', t2)

# creating a tuple from a string
t1 = tuple('Python')
print('t1 =',t1)

# creating a tuple from a dictionary
t1 = tuple({1: 'one', 2: 'two'})
print('t1 =',t1)

#
languages = ('Python', 'Swift', 'C++')

# access the first item
print(languages[0])   # Python

# access the third item
print(languages[2])   # C++

cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
print('Total Items:', len(cars))

# Output: Total Items: 4

fruits = ('apple','banana','orange')

# iterate through the tuple
for fruit in fruits:
    print(fruit)

colors = ('red', 'orange', 'blue')

print('yellow' in colors)
print('orange' in colors)


fruits = ('apple', 'cherry', 'orange')

# trying to change the second item to 'banana'
# fruits[1] = 'banana'

print(fruits)

print("fruits count", fruits.count('cherry'))

print("index of fruit", fruits.index('orange'))

# Output: TypeError: 'tuple' object does not support item assignment

animals = ('dog', 'cat', 'rat')

# deleting the tuple
del animals

# print(animals)

var = ('Hello',)
print(var)  # tuple

# Output: ('Hello',)

