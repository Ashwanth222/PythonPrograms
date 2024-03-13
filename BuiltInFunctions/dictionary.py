my_dict = {
    'name' : 'name1',
    "age"  : 34,
    "salary": 3453.453,
    "isMarried" : False,
    "friends" : ['jay', 'tej', 'chai', 'lju']
}

print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('age'))
my_dict.pop('salary')
print(my_dict)
my_dict.update({
    'name' : 'name1',
    "age"  : 35,
    "isMarried" : False
})
print(my_dict)

my_dict.update({
    'name' : 'name1',
    "age"  : 35,
    "salary": 45.67,
    "isMarried" : False
})
print(my_dict)

print(my_dict["salary"])

print(my_dict['friends'][2])
print(my_dict['friends'][2][2])

print(type[my_dict])

print(type(my_dict))

print(my_dict.items())

print(my_dict.popitem())
print(my_dict)

my_dict2 = my_dict.copy()
print(my_dict2)

my_dict2.clear()
print(my_dict2)
print(type(my_dict))