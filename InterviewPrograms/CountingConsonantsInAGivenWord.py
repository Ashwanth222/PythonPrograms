vowels = ['a', 'e', 'i', 'o', 'u']
string = 'string in a program'
count = 0
for character in string:
    if character not in vowels:
        count = count +1

print(count)