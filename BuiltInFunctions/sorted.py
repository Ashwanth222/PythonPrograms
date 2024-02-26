numbers = [4, 2, 12, 8]

# sort the list in ascending order
sorted_numbers = sorted(numbers)

print(sorted_numbers)

# Output: [2, 4, 8, 12]

# list of vowels in random order
vowels_list = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
print('Sorted Vowels:', sorted(vowels_list))

# Output: Sorted Vowels: ['a', 'e', 'i', 'o', 'u']

numbers = [2, 7, 3, 9, 13, 11]

# sorting the numbers in descending order
sorted_numbers = sorted(numbers, reverse=True)

print(sorted_numbers)

# Output: [13, 11, 9, 7, 3, 2]

fruits = ['apple', 'banana', 'kiwi', 'pomegranate']

# sorts the list based on the length of each string
sorted_fruits = sorted(fruits, key=len)

print('Sorted list:', sorted_fruits)

# Output: Sorted list: ['kiwi', 'apple', 'banana', 'pomegranate']

numbers = [3, 1, 4, 1, 5, 9, 2, 5, 3]

# sort using sort() method
numbers.sort()

print("Using sort():", numbers)

# Output: Using sort(): [1, 1, 2, 3, 3, 4, 5, 5, 9]

numbers = [3, 1, 4, 1, 5, 9, 2, 5, 3]

# sort using sorted() method
sorted_numbers = sorted(numbers)

print("Using sorted():", sorted_numbers)

print("Original list:", numbers)

# =============


personal_info = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]

def get_age(person):
    return person[1]

personal_info.sort(key=get_age)

print(personal_info)

personal_infoo = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
def get_agge(person):
    return person[1]

personal_infoo.sort(key=get_agge)

personal_infoo.reverse()
print(personal_infoo)