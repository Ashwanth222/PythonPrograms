
prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

# Output:
# Removed Element: 5
# Updated List: [2, 3, 7]

# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)

print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)

# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:')
print('Return Value:', languages.pop())

print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:')
print('Return Value:', languages.pop(-1))

print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:')
print('Return Value:', languages.pop(-3))

print('Updated List:', languages)