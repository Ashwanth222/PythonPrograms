a = [3,7,9,2,5]
b = iter(a)
print(b.__next__())
print(b.__next__())
print(next(b))
print(next(b))

#
c = [7,3,8,2,9]
for elements in c:
    print(elements)

#

e = [7, 8, 2, 4, 1, 3]

ite = iter(e)

for element in ite:
    print(element)

#
"""Class to implement an iterator
 """

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i)) # prints 1
print(next(i)) # prints 2
print(next(i)) # prints 4
print(next(i)) # prints 8
# print(next(i)) # raises StopIteration exception

#

from itertools import count

# create an infinite iterator that starts at 1 and increments by 1 each time
infinite_iterator = count(1)
print(infinite_iterator)

# print the first 5 elements of the infinite iterator
for i in range(5):
    print(next(infinite_iterator))


for i in PowTwo(3):
    print(i)











