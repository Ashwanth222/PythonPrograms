myDict = {'ravi': 10, 'rajnish': 9,
          'sanjeev': 15, 'yash': 2, 'suraj': 32}

sorted(myDict)

keys = list(myDict.keys())

keys.sort()

for i in keys:
 print(i, myDict[i])

 # sort using values ascending order

 values = list(myDict.values())

values.sort()

for i in values:
    print(i)

# descending order

newValues = sorted(values, reverse=True)
for i in newValues:
    print("values", i)

# sort keys in descending order

newKeys = sorted(keys, reverse=True)
for i in newKeys:
    print(i, newKeys.index(i))
# sort keys in ascending order

newKeys = sorted(keys, reverse=False)
for i in newKeys:
    print(i)

#
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)

#
def dictionary():
    key_value = {}

    key_value[0] = 1
    key_value[1] = 2
    key_value[2] = 3
    key_value[3] = 4
    key_value[4] = 5

    for i in sorted(key_value.keys()):
        print(i, key_value[i])

def main():
    dictionary()

# main function calling
if __name__ == "__main__":
    main()

#

# Function calling
def dictionairy():

    # Declaring hash function
    key_value = {}

    # Initializing the value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("key_value",key_value)

    print("Task 3:-\nKeys and Values sorted",
          "in alphabetical order by the value")

    # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
    print(sorted(key_value.items(), key=lambda kv:
    (kv[1], kv[0])))


def main():
    # function calling
    dictionairy()


# main function calling
if __name__ == "__main__":
    main()



# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict
import numpy as np

dict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)

keyss = list(dict.keys())

valuess = list(dict.values())

sorted_value_index = np.argsort(valuess)

sorted_dict = {keys[i] : values[i] for i in sorted_value_index}

print(sorted_dict)




