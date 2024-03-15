str = "this is python"
ch_iterator = iter(str)
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))

#

# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

# An iterable user defined type
class Test:

    # Constructor
    def __init__(self, limit):
        self.limit = limit

    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):

        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1;
        return x

# Prints numbers from 10 to 15
for i in Test(15):
    print(i)

# Prints nothing
for i in Test(5):
    print(i)


#
# Sample built-in iterators

# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

#  iterating over a dictionary
print("iterating in dictionary")
d = dict()
d[1] = "123"
d[2] = "234"
for i in d:
    print("i, d[i] =", i, d[i])


# iterating in tuple
tup = ('a', 'b', 'c', 'd', 'e')
for i in tup:
    print(i)

#
tup = ('a', 'b', 'c', 'd', 'e')
it = iter(tup)
print("inside loop")
for index,i in enumerate(it):
    print(i)
    if index ==2:
        break

# we can print the remaining items to be iterated using next()
# thus, the state was saved
print("outside loop")
print(next(it))
print(next(it))

#
iterable = (1, 2, 3, 4)
iterator_obj = iter(iterable)

print("Iterable loop 1:")
# iterating on iterable
for ite in iterable:
    print(ite)

print("Iterable loop 1:")
# iterating on iterable
for ite in iterable:
    print(ite)

print("\nIterating on an iterator:")
# iterating on an iterator object multiple times
for item in iterator_obj:
        print(item, end=",")

print("\nIterator: Outside loop")
# this line will raise StopIteration Exception
# since all items are iterated in the previous for-loop
# print(next(iterator_obj))
# StopIteration

#




