import re

s = "python is a programming. language"
match = re.search(r'language', s)
print('Start Index:', match.start())
print('End Index:', match.end())

# without using \
ser = re.search(r'.', s)
print(ser)

# using \
serc = re.search(r'\.', s)
print(serc)

# using [ ]
result = re.findall('[a-m]',s)
print(result)

# using ^

regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
    if re.match(regex, string):
        print(f"match found for", {string})
    else:
        print(f'match not found for', {string})

# using $

string = "Hello World!"
regex = r"World!$"
sear = re.search(regex, string)
if sear:
    print(f"found  at end{string}")
else:
    print(f"no match found at end", {string})

# using .

string = "The quick brownfox jumps over the lazy dog."
regex = r"brown.fox"
match = re.match(regex, string)
if match:
    print("found for", {string})
else:
    print("not found for", {string})

# using '\d+'

string = """Hello my Number is 123456789 and 
            my friend's number is 987654321"""
regex = '\d+'

found = re.findall(regex, string)
print(found)

# using []
y = "Aye, said Mr. Gibenson Stark"
compilee = re.compile('[a-e]')
found = compilee.findall(y)
print(found)

# using /d

regex = re.compile('\d')
searchh = regex.findall("I went to him at 11 A.M. on 4th July 1886")
print(searchh)

regex = re.compile('\d+')
searchh = regex.findall("I went to him at 11 A.M. on 4th July 1886")
print(searchh)

# using \w
regex = re.compile('\w')
searchh = regex.findall("I went to him at 11 A.M., he \
    said *** in some_language.")
print(searchh)

regex = re.compile('\w+')
searchh = regex.findall("I went to him at 11 A.M., he \ said *** in some_language.")
print(searchh)

regex = re.compile('\W')
searchh = regex.findall("I went to him at 11 A.M., he \ said *** in some_language.")
print(searchh)

regex = re.compile('\W+')
searchh = regex.findall("I went to him at 11 A.M., he \ said *** in some_language.")
print(searchh)

# using \a*
# The code uses a regular expression pattern ‘ab*’ to find and list all occurrences of
# ‘ab’ followed by zero or more ‘b’ characters in the input string “ababbaabbb”.
# It returns the following list of matches: [‘ab’, ‘abb’, ‘abbb’].


regex = re.compile('ab*')
searchh = regex.findall("ababbaabbb")
print( "searchh", searchh)

# using split

print(re.split('\W', 'Words, words, Words'))
print(re.split('\W+', 'Words, words, Words'))
print(re.split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM'))
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
print(re.split('[a-f]+', 'On 12th Jan 2016, at 11:02 AM'))
print(re.split('[a-f]+', 'On 12th Jan 2016, at 11:02 AM', flags=re.IGNORECASE))

# using sub (substitute)

print(re.sub('ub', '*&', 'Subject has Uber booked already'))
print(re.sub('ub', '*&', 'Subject has Uber booked already', flags=re.IGNORECASE))
print(re.sub('ub', '*&', 'Subject has Uber booked already', count=1, flags=re.IGNORECASE))
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',
             flags=re.IGNORECASE))

# using subn (substitute)

import re

print(re.subn('ub', '~*', 'Subject has Uber booked already'))

t = re.subn('ub', '~*', 'Subject has Uber booked already',
            flags=re.IGNORECASE)
print(t)
print(len(t))
print(t[0])

# using escape


print(re.escape("hi this is somethig"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))

# re.search()

regex = r'([a-zA-Z]+) (\d+)'
match = re.search(regex, "I was born on June 24")
if match!= None:
    print(match.start(), match.end())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
else:
    print ("The regex pattern does not match.")


# SETS
# match

s = "Welcome to GeeksForGeeks"
search = re.search(r"\bG", s)
print(search.re)
print(search.start())
print(search.end())
print(search.string)

s = "Welcome to GeeksForGeeks"
search = re.search(r"\bGee", s)
print(search.start())
print(search.end())
print(search.group(0))
print(search.span())

s = "Welcome to GeeksForGeeks"
search = re.search(r"\D{2} t", s)
print(search.group())




