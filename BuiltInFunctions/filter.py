def even_number(numbers):
    if numbers % 2 == 0:
        return True
    else:
        return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(even_number, numbers)

print(list(even_numbers))

# find vowels
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
def find_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter in vowels:
        return True
    else:
        return False



vowels_in = filter(find_vowel, letters)
print(tuple(vowels_in))


# find even numbers using lambda
numbers = [1, 2, 3, 4, 5, 6, 7]

even = filter(lambda x: (x % 2 == 0), numbers)

print(list(even))

# filter None
random_list = [1, 'a', 0, False, True, '0']
filtered_iterator = filter(None, random_list)

# converting to list
filtered_list = list(filtered_iterator)

print(filtered_list)

# Output: [1, 'a', True, '0']




