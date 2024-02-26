numbers = [9, 34, 11, -4, 27]

# find the smallest number
min_number = min(numbers)
print(min_number)

# Output: -4

number = [3, 2, 8, 5, 10, 6]
smallest_number = min(number);

print("The smallest number is:", smallest_number)

languages = ["Python", "C Programming", "Java", "JavaScript"]
smallest_string = min(languages);

print("The smallest string is:", smallest_string)

square = {2: 4, 3: 9, -1: 1, -2: 4}

# the smallest key
key1 = min(square)
print("The smallest key:", key1)    # -2

# the key whose value is the smallest
key2 = min(square, key = lambda k: square[k])

print("The key with the smallest value:", key2)    # -1

# getting the smallest value
print("The smallest value:", square[key2])    # 1

result = min(4, -5, 23, 5)
print("The minimum number is:", result)

numbers = [1,2,3,4]
def square(number):
    return number*number

num = map(square, numbers)

def square(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(square, numbers)
print(result)

# converting the map object to set
result = set(result)
print(result)

li = list(num)
print("list of",li)

def square(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(square, numbers)
print(result)

# converting the map object to set
result = set(result)
print(result)

numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# convert to set and print it
print(set(result))

num1 = [1, 2, 3]
num2 = [10, 20, 40]

res = map(lambda n1, n2: n1+n2, num1, num2)
print(list(res))
print(set(res))

# list of actions
actions=['eat', 'sleep','read']
print(list(map(list,actions)))




