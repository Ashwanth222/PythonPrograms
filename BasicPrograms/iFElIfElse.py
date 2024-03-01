a = 'Fallse'
a = False
name = 'Tim'

if a != True:
    print('a is false')
else:
    print("a is true")

# if elif and else
if a != True and name != 'Tim':
    print("neither a is true nor name is tim")
elif a == False or name != 'Tim':
    print("either a is true or name is tim")
else:
    print("is in else statement")