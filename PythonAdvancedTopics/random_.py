import random
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))


# random.seed(5)
print(random.random())
print(random.random())

r1 = random.randint(5, 16)
print("Random number between 5 and 16 is % s" % (r1))
r2 = random.randint(-10, -2)
print("Random number between -10 and -2 is % d" % (r2))

# random.randrange(1,9)
from random import random

print(random())

import random

print(random.choices([2,6]))

print(random.randbytes(4))

li = [2,5,8,3,6,9]
print(random.choice(li))

tuple = (2,5,8,6,4,9,3)
print(random.choice(tuple))

str = "string"
print(random.choice(str))

from random import sample
list1 = [1, 2, 3, 4, 5]

print(sample(list1,3))
list2 = (4, 5, 6, 7, 8)

print(sample(list2,3))
list3 = "45678"

print(sample(list3,3))

import random
sample_list = [1, 2, 3, 4, 5]

print("Original list : ")
print(sample_list)
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)




