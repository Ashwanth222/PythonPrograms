try:
   x = int(input("enter a number"))
   print(x)
except:
    print('number is not an integer')


#

try:
    x = int(input("enter a number"))
    print(x)
except ValueError:
    print('number is not an integer')

    #

try:
    x = int(input("enter a number"))
    print(x)
except ValueError:
    print('number is not an integer')
finally:
    print('is in finally block')