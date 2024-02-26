numbers1 = [1, 4]

numbers2 = [2, 3, 5]

# add the elements of numbers2 list to numbers1
numbers1.extend(numbers2)

print('numbers1 =', numbers1)

# Output: numbers1 = [1, 4, 2, 3, 5]

# languages list
languages = ['French', 'English']

# another list of language
languages1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
languages.extend(languages1)

print('Languages List:', languages)

#

# languages list
languages = ['French']

# languages tuple
languages_tuple = ('Spanish', 'Portuguese')

# languages set
languages_set = {'Chinese', 'Japanese'}

# appending language_tuple elements to language
languages.extend(languages_tuple)

print('New Language List:', languages)

# appending language_set elements to language
languages.extend(languages_set)

print('Newer Languages List:', languages)

# other way of extending

a = [1, 2]
b = [3, 4]

a += b    # a = a + b

# Output: [1, 2, 3, 4]
print('a =', a)

# =========================

a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

# a1 = [1, 2, 3, 4]
a1.extend(b)
print(a1)

# a2 = [1, 2, (3, 4)]
a2.append(b)
print(a2)