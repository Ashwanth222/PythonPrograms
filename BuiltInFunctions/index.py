# tuple containing vowels
vowels = ('a', 'e', 'i', 'o', 'u')

# index of 'e' in vowels
index = vowels.index('e')

print(index)

# Output: 1

# alphabets tuple
alphabets = ('a', 'e', 'i', 'o', 'g', 'l', 'i', 'u')

# returns the index of first 'i' in alphabets
index = alphabets.index('i')

print('Index of i in alphabets:', index)

# scans 'i' from index 4 to 7 and returns its index
index = alphabets.index('i', 4, 7)

print('Index of i in alphabets from index 4 to 7:', index)