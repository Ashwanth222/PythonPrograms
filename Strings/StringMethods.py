s = "   hellohello "
print(s[4])
print(s[-4])
print(s.lower().upper().capitalize().casefold())
print(s.upper())
print(s.capitalize())
print(s.casefold())
print(s.isalnum())
print(s.isascii())
print(s.isdigit())
print(s.isdecimal())
print(s.istitle())
print(s.removeprefix("he"))
print(s.join("hello"))
print("s.lstrip()",s.lstrip())
print(s.removesuffix("llo"))
print(s.swapcase())
print(s.splitlines())
print(s.replace(s,"helli"))
print(s.__contains__("a"))
print(s.__len__())
print(s.partition("l"))
# print(s.format_map("a"))
print(s.strip())
print(s.__add__("hell"))
print(s.__sizeof__())
print(s.__eq__("   hellohello "))
print(s.rstrip())
print(s.rsplit("e"))
print(s.rpartition("e"))
# print(s.splitlines())
# print("123".__reduce__().join('56'))
# print(s.__init__())
# print(s.isspace().conjugate())
print(s.endswith("lo  "))
print(s.find('h'))
# print(s.translate())
# print(s.__format__("z"))
print(s[1:4])  # "ell"
print("s.startswith(' ')",s.startswith(' '))

# multiline string
message = """
Never gonna give you up
Never gonna let you down
Never gonna let you down
"""

print(message)

str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)

greet = "Hello, "
name = "Jack"

# using + operator
result = greet + name
print(result)

# Output: Hello, Jack

greet = 'Hello'

# iterating through greet string
for letter in greet:
    print(letter)

greet = 'Hello'

# count length of greet string
print(len(greet))

# Output: 5

print('a' in 'program') # True
print('at' not in 'battle') # False

s = " hi how ae you? \'it's me\'"
print(s)

# escape double quotes
example = "He said, \"What's there?\""
print(example)

# escape single quotes
example = 'He said, "What\'s there?"'

print(example)

name = 'Cathy'
country = 'UK'

print(f'{name} is from {country}')

# Output: He said, "What's there?"