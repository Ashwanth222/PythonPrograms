
# Python program to sort dictionary
# by value using lambda function

# Initialize a dictionary
my_dict = {2: 'three',
           1: 'two'}

# Sort the dictionary
sorted_dict = sorted(
    my_dict.items(),
    key = lambda kv: kv[1])

print(sorted_dict)

#


# Python program to sort dictionary
# by value using item function

# Initialize a dictionary
my_dict = {'c': 3,
           'a': 1,
           'd': 4,
           'b': 2}

# Sorting dictionary
sorted_dict = sorted([(value, key)
    for (key, value) in my_dict.items()])

# Print sorted dictionary
print("Sorted dictionary is :")
print(sorted_dict)

# Python program to sort dictionary
# by value using sorted() and get()

# Initialize a dictionary
my_dict = {'red': '# FF0000', 'green': '# 008000',
           'black': '# 000000', 'white': '# FFFFFF'}

for w in sorted(my_dict, key = my_dict.get):
    print(w, my_dict[w])

# Python program to sort dictionary
# by value using itemgetter() function

# Importing OrderedDict
import operator

# Initialize a dictionary
my_dict = {'a': 23,
           'g': 67,
           'e': 12,
           45: 90}

# Sorting dictionary
sorted_dict = sorted(my_dict.items(), \
                     key = operator.itemgetter(1))

# Printing sorted dictionary
print("Sorted dictionary is :")
print(sorted_dict)

# Python program to sort dictionary
# by value using OrderedDict

# Import OrderedDict
from collections import OrderedDict

# Initialize a dictionary
my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Sort dictionary
sorted_dict = OrderedDict(sorted( \
    my_dict.items(), key = lambda x: x[1]))

# Print the sorted dictionary
print("Sorted dictionary is :")
print(sorted_dict)

# Python program to sort dictionary
# by value using OrderedDict

# Import Counter
from collections import Counter

# Initialize a dictionary
my_dict = {'hello': 1, 'python': 5, 'world': 3}

# Sort and print the dictionary
sorted_dict = Counter(my_dict)
print("Sorted dictionary is :")
print(sorted_dict.most_common()[::-1])

# Python program to sort dictionary
# by value using sorted setting
# reverse parameter to true

# Initialize a dictionary
my_dict = {'red': '# FF0000', 'green': '# 008000',
           'black': '# 000000', 'white': '# FFFFFF'}

# Sort and print the dictionary
print("Sorted dictionary is :")
for w in sorted(my_dict, key = my_dict.get, \
                reverse = True):
    print(w, my_dict[w])

