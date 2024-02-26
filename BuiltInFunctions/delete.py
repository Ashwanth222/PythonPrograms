my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# deleting the third item
del my_list[2]

# Output: [1, 2, 4, 5, 6, 7, 8, 9]
print(my_list)

# deleting items from 2nd to 4th
del my_list[1:4]

# Output: [1, 6, 7, 8, 9]
print(my_list)

# deleting all elements
del my_list[:]

# Output: []
print(my_list)


person = { 'name': 'Sam',
           'age': 25,
           'profession': 'Programmer'
           }

del person['profession']

# Output: {'name': 'Sam', 'age': 25}
print(person)


# Note: You can't delete items of tuples and strings in Python. It's because tuples and strings are immutables; objects that can't be changed after their creation.
#
# my_tuple = (1, 2, 3)
#
# # Error: 'tuple' object doesn't support item deletion
# del my_tuple[1]
# However, you can delete an entire tuple or string.
#
#
# my_tuple = (1, 2, 3)
#
# # deleting tuple
# del my_tuple