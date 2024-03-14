word = 'python programming'
occurance = 0
character = 'p'

for char in word:
    if char.__contains__(character):
        occurance = occurance + 1

print(occurance)

# alternate
count = 0
for char in word:
    if char == character:
        count = count + 1

print(count)