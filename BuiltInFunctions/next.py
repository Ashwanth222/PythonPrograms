marks = [65, 71, 68, 74, 61]
print(iter(marks).__next__())
print(iter(marks).__next__())

next_iterator = iter(marks)
print(next(next_iterator))
print(next(next_iterator))

marks = [65, 71, 68, 74, 61]

# convert list to iterator
iterator_marks = iter(marks)

# the next element is the first element
marks_1 = next(iterator_marks)
print(marks_1)

# find the next element which is the second element
marks_2 = next(iterator_marks)
print(marks_2)

# Output: 65
#         71

random = [5, 9, 'cat']

# converting the list to an iterator
random_iterator = iter(random)
print(random_iterator)

# Output: 5
print(next(random_iterator))

# Output: 9
print(next(random_iterator))

# Output: 'cat'
print(next(random_iterator))

# This will raise Error
# iterator is exhausted
# print(next(random_iterator))

random = [5, 9]

# converting the list to an iterator
random_iterator = iter(random)

# Output: 5
print(next(random_iterator, '-1'))

#random bytearray
random_byte_array = bytearray('ABC', 'utf-8')

mv = memoryview(random_byte_array)

# access memory view's zeroth index
print(mv[0])

# create byte from memory view
print(bytes(mv[0:2]))

# create list from memory view
print(list(mv[0:3]))

# Output: 9
print(next(random_iterator, '-1'))

# random_iterator is exhausted
# Output: '-1'
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))

# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')
print('Before updation:', random_byte_array)

mv = memoryview(random_byte_array)

# update 1st index of mv to Z
mv[1] = 90
print('After updation:', random_byte_array)
