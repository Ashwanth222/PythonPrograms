
# Merging Two Dictionaries in Python
# There are various ways in which Dictionaries can be merged by using various functions and constructors in Python. Below are some following ways:
#
# Using update()
# Using unpacking operator
# Using merge | operator
# Using loops and keys() method
# Using dict constructor
# Using the dict() constructor with the union operator (|)
# Using reduce()

# update
def merge(dict1,  dict2):
    return dict1.update(dict2)

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

merge(dict1,dict2)
print(dict1)

# unpack operator
def mergee(dict1, dict2):
    res = {**dict1, **dict2}
    return res

dict1 = {'a': 12, 'b': 18}
dict2 = {'d': 16, 'c': 14}

res = mergee(dict1, dict2)
print(res)

# |

def mergeee(dict1, dict2):
    res = dict1 | dict2
    return res

dict1 = {'a': 19, 'b': 28}
dict2 = {'d': 46, 'c': 74}

res = mergeee(dict1, dict2)
print(res)

#using loops and keys operator

def mergee(dict1, dict2):
    for i in dict2.keys():
     dict1[i] = dict2[i]
    return dict1

dict1 = {'a': 32, 'b': 38}
dict2 = {'d': 36, 'c': 34}

res = mergee(dict1, dict2)
print(res)

# Using dict constructor

def merge_dictionaries(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3

# Driver code
dict1 = {'x': 15, 'y': 18}
dict2 = {'a': 116, 'b': 14}

ress = merge_dictionaries(dict1, dict2)

print(ress)

# Using the dict() constructor with the union operator (|)

def Merge(dict1, dict2):
    dict3 = dict(dict1.items()| dict2.items())
    return dict3
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# merge the two dictionaries using the Merge() function
merged_dict = Merge(dict1, dict2)

# print the merged dictionary
print(merged_dict)


#

from functools import reduce

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

listt = [dict1, dict2]

result = reduce(merge_dictionaries, listt)

print(result)

# 