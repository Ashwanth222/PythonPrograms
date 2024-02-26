numbers = [9, 34, 11, -4, 27]

# find the maximum number
max_number = max(numbers)
print(max_number)

# Output: 34

number = [3, 2, 8, 5, 10, 6]
largest_number = max(number);

print("The largest number is:", largest_number)

languages = ["Python", "C Programming", "Java", "JavaScript"]
largest_string = max(languages)

print("The largest string is:", largest_string)

square = {2: 4, -3: 9, -1: 1, -2: 4}

# the largest key
key1 = max(square)
print("The largest key:", key1)    # 2

# the key whose value is the largest
key2 = max(square, key = lambda k: square[k])

print("The key with the largest value:", key2)    # -3

# getting the largest value
print("The largest value:", square[key2])    # 9

