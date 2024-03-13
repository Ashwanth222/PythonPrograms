d = {'a':1, 'b':4}

# trying to output value of absent key
print ("The value associated with 'c' is : ")
# print(d['c'])


ele = {'a': 5, 'c': 8, 'e': 2}

if 'd' in ele:
    print(d)
else:
    print('key not found')

#
country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

print(country_code.get('India', 'Not found'))
print(country_code.get('Japan', 'Not found'))

country_code.setdefault('Japan', 'Not present')
print(country_code.get('India'))
print(country_code.get('Japan'))

import collections

defd = collections.defaultdict(lambda : 'key not found')

defd['a'] = 1

defd['b'] = 2

#
defd['c'] = 3

print('the value present in a is', defd['a'])
print('the value present in d is', defd['d'])


#
country_code = {'India': '0091',
                'Australia': '0025',
                'Nepal': '00977'}

try:
    print(country_code['India'])
    print(country_code['USA'])
except:
    print('Not found')

#
# Python code to demonstrate a dictionary
# with multiple inputs in a key.
import random as rn

# creating an empty dictionary
dict = {}

# Insert first triplet in dictionary
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z;

# Insert second triplet in dictionary
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z;

# print the dictionary
print(dict)

# dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"):"Mumbai", \
          ("28.33'34.1", "77.06'16.6"):"Delhi"}

print(places)
print('\n')

# Traversing dictionary with multi-keys and creating
# different lists from it

lat = []
long = []
plc = []
for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i[0], i[1]])

print(lat)
print(long)
print(plc)

#
# Creating a dictionary with multiple inputs for keys
data = {
    (1, "John", "Doe"): {"a": "geeks", "b": "software", "c": 75000},
    (2, "Jane", "Smith"): {"e": 30, "f": "for", "g": 90000},
    (3, "Bob", "Johnson"): {"h": 35, "i": "project", "j": "geeks"},
    (4, "Alice", "Lee"): {"k": 40, "l": "marketing", "m": 100000}
}

print(data[(1, "John", "Doe")]['a'])
print(data[(3, "Bob", "Johnson")]['i'])
print(data[(4, "Alice", "Lee")]['k'])

data[(1, "John", "Doe")]["a"] = {"b": "marketing", "c": 75000}
data[(3, "Bob", "Johnson")]["j"] = {"h": 35, "i": "project"}
print(data[(1, "John", "Doe")]["a"])
print(data[(3, "Bob", "Johnson")]["j"])


