text = 'Python Programing'

# get slice object to slice Python
sliced_text = slice(7)
print(text[sliced_text])
print(text[slice(3,7)])

# Output: Python

# slice() Syntax
# The syntax of slice() is:
#
# slice(start, stop, step)

# slice() Parameters
# slice() can take three parameters:
#
# start (optional) - Starting integer where the slicing of the object starts.
# Default to None if not provided.
# stop - Integer until which the slicing takes place.
# The slicing stops at index stop -1 (last element).
# step (optional) - Integer value which determines the increment
# between each index for slicing. Defaults to None if not provided.
print(text[slice(3,8,4)])

# Program to get a substring from the given string

py_string = 'Python'

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3)
print(py_string[slice_object])  # Pyt

# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6, 2)
print(py_string[slice_object])   # yhn

py_string = 'Python'

# start = -1, stop = -4, step = -1
# contains indices -1, -2 and -3
slice_object = slice(-1, -4, -1)

print(py_string[slice_object])   # noh

py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices 0, 1 and 2
slice_object = slice(3)
print(py_list[slice_object]) # ['P', 'y', 't']

# contains indices 1 and 3
slice_object = slice(1, 5, 2)
print(py_tuple[slice_object]) # ('y', 'h')

py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices -1, -2 and -3
slice_object = slice(-1, -4, -1)
print(py_list[slice_object])  # ['n', 'o', 'h']

# contains indices -1 and -3
slice_object = slice(-1, -5, -2)
print(py_tuple[slice_object]) # ('n', 'h')

py_string = 'Python'

# contains indices 0, 1 and 2
print(py_string[0:3])  # Pyt

# contains indices 1 and 3
print(py_string[1:5:2]) # yh
