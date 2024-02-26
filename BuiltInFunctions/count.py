# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]

# check the count of 2
count = numbers.count(2)

print('Count of 2:', count)

# Output: Count of 2: 3

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)

#
# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("The count of [3, 4] is:", count)

# tuple count

# tuple of numbers
numbers = (1, 3, 4, 1, 6 ,1 )

# counts the number of 1's in the tuple
count = numbers.count(1)

print('The count of 1 is:', count)

# counts the number of 7's in the tuple
count = numbers.count(7)

print('The count of 7 is:', count)