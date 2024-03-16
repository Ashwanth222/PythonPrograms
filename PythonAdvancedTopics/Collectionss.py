# A Python program to show different 
# ways to create Counter 
from collections import Counter

# With sequence of items 
print(Counter(['B','B','A','B','C','A','B',
               'B','A','C']))

# with dictionary 
print(Counter({'A':3, 'B':5, 'C':2}))

# with keyword arguments 
print(Counter(A=3, B=5, C=2))

# OrderedDict

d = {}

d[0] = 1
d[1] = 2
d[2] = 3
d[3] = 4

for key, value in d.items():
    print(key, value)


from collections import OrderedDict

d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

print("\nThis is an Ordered Dict:\n")
for key, value in d.items():
    print("OrderedDict", key, value)

d.pop('a')

for key, value in d.items():
    print("pop", key, value)

d.popitem()

for key, value in d.items():
    print("popitem", key, value)

d['a'] = 1

for key, value in d.items():
    print("after inserting", key, value)

# DefaultDict

from collections import defaultdict

L = [2,3,4,5,1,2,3,4,5,3,2,1,5,4,2,3,1]

d = defaultdict(int)

for i in L:
    d[i] +=1

print(d)

#

d = defaultdict(list)
for i in range(5):
    d[i].append(i)

print(d)

from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

d = ChainMap(d1, d2, d3)
print(d)

#

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

c = ChainMap(d1, d2, d3)
# Accessing values using values()
# method
print(c.values())

#

# Python code to demonstrate ChainMap and
# new_child()

import collections

# initializing dictionaries
dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }
dic3 = { 'f' : 5 }

# initializing ChainMap
chain = collections.ChainMap(dic1, dic2)

# printing chainMap
print ("All the ChainMap contents are : ")
print (chain)

# using new_child() to add new dictionary
chain1 = chain.new_child(dic3)

# printing chainMap
print ("Displaying new ChainMap : ")
print (chain1)

from collections import namedtuple

Student = namedtuple("Student", ("name", "age", "salary"))

S= Student("name", 23, 34564)

print(S[1])

print(S.name)

# Conversion Operations

from collections import namedtuple

Student = namedtuple("Student", ("name", "age", "salary"))

S = Student("name", 23, 34564)

# initializing iterable
li = ['Manjeet', '19', '411997' ]

# initializing dict
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }

# using _make() to return namedtuple()
print ("The namedtuple instance using iterable is  : ")
print (Student._make(li))

# using _asdict() to return an OrderedDict()
print ("The OrderedDict instance using namedtuple is  : ")
print (S._asdict())

# deque

# Python code to demonstrate deque

from collections import deque

# Declaring deque
queue = deque(['name','age','DOB'])

print(queue)

# Python code to demonstrate working of
# append(), appendleft()


from collections import deque

# initializing deque
de = deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("The deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("The deque after appending at left is : ")
print(de)

# Python code to demonstrate working of
# pop(), and popleft()

from collections import deque

# initializing deque
de = deque([6, 1, 2, 3, 4])

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("The deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("The deque after deleting from left is : ")
print(de)

# UserDict

# Python program to demonstrate
# userdict


from collections import UserDict


# Creating a Dictionary where
# deletion is not allowed
class MyDict(UserDict):

    # Function to stop deletion
    # from dictionary
    # def __del__(self):
    #     raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # dictionary
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop popitem
    # from Dictionary
    # def popitem(self, s = None):
    #     raise RuntimeError("Deletion not allowed")

    # Driver's code
d = MyDict({'a':1,
            'b': 2,
            'c': 3})

# d.pop(1)

# UserList

# Python program to demonstrate
# userlist


from collections import UserList


# Creating a List where
# deletion is not allowed
class MyList(UserList):

    # Function to stop deletion
    # from List
    def remove(self, s = None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # List
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")

    # Driver's code
L = MyList([1, 2, 3, 4])

print("Original List")

# Inserting to List"
L.append(5)
print("After Insertion")
print(L)

# Deleting From List
# L.remove()


# UserString

# Python program to demonstrate
# userstring


from collections import UserString


# Creating a Mutable String
class Mystring(UserString):

    # Function to append to
    # string
    def append(self, s):
        self.data += s

    # Function to remove from
    # string
    def remove(self, s):
        self.data = self.data.replace(s, "")

    # Driver's code
s1 = Mystring("Geeks")
print("Original String:", s1.data)

# Appending to string
s1.append("s")
print("String After Appending:", s1.data)

# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)










