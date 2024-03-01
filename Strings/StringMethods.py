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

sk = "string"

print(sk.upper())

print(sk.join("kkk"))

print(sk.partition("r"))

# example dictionary
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))

# example dictionary
dict = {97: "123", 98: "456", 99: "789"}
string = "abc"
print(string.maketrans(dict))

# first string
firstString = "abc"
secondString = "def"
thirdString = "abd"
string = "abc"
print(string.maketrans(firstString, secondString, thirdString))

# first string
firstString = "abc"
secondString = "def"
string = "abc"
print(string.maketrans(firstString, secondString))

# example dictionary
# firstString = "abc"
# secondString = "defghi"
# string = "abc"
# print(string.maketrans(firstString, secondString))

#   print(string.maketrans(firstString, secondString))
# ValueError: the first two maketrans arguments must have equal length

quote = 'Let it be, let it be, let it be'

result = quote.rindex('let it')
print("Substring 'let it':", result)

# result = quote.rindex('small')
# print("Substring 'small ':", result)

# output
#  result = quote.rindex('small')
# ValueError: substring not found

quote = 'Do small things with great love'

# Substring is searched in ' small things with great love'
print(quote.rindex('t', 2))

# Substring is searched in 'll things with'
print(quote.rindex('th', 6, 20))

# # Substring is searched in 'hings with great lov'
# print(quote.rindex('o small ', 10, -1))

quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it':", result)

result = quote.rfind('small')
print("Substring 'small ':", result)

result = quote.rfind('be,')
if  (result != -1):
    print("Highest index where 'be,' occurs:", result)
else:
    print("Doesn't contain substring")

quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.rfind('things', 10))

# Substring is searched in ' small things with great love'
print(quote.rfind('t', 2))

# Substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.rfind('th', 6, 20))

countries = ['united kingdon', 'india', 'america', 'kenya', 'netherlands', 'australia']
print(countries[2][3])

print(type(countries[2][4]))

print(countries[-2])

all = ['india', 'china', 'bangladesh', 234, True, False, 43]

print(type[all[4]])

print(type[all])
print(type(all))

print(type(all[3]))

