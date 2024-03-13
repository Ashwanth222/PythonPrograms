
# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])

    final = sum(list)
    return final

s = {'a':100, 'b':200, 'c':300}
print(returnSum(s))

#

def returnSum(dict):

    sum = 0
    for i in dict.values():
        sum = sum + i
    print(sum)
    return sum

# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

#
def returnSumm(dict):

    sum = 0
    for i in dict:
        sum = sum + dict[i]
    print(sum)
    return sum

# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSumm(dict))


# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(dict):
    return sum(dict.values())


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

import functools

dic = {'a': 100, 'b': 200, 'c': 300}

sum_dic = functools.reduce(lambda ac, k: ac+ dic[k], dic, 0)

print('sum_dic', sum_dic)

#
def returnSum(dict):
    return sum(dict[key] for key in dict)

dict = {'a': 100, 'b': 200, 'c': 300}
print("k Sum :", returnSum(dict))

#

import functools

def sum_dict_values(dict):
    return functools.reduce(lambda acc , x: acc + dict[x], dict, 0 )

# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum ::", sum_dict_values(dict))


#

import numpy as np

# function to return sum
def returnSum(dict):
    # convert dict values to a NumPy array
    values = np.array(list(dict.values()))
    # return the sum of the values
    return np.sum(values)

# driver code
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum:::", returnSum(dict))


import sys

# sample Dictionaries
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

# print the sizes of sample Dictionaries
print("Size of dic1: " + str(sys.getsizeof(dic1)) + "bytes")
print("Size of dic2: " + str(sys.getsizeof(dic2)) + "bytes")
print("Size of dic3: " + str(sys.getsizeof(dic3)) + "bytes")