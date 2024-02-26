number = 13.46

# round 13.46 to the nearest integer
rounded_number = round(number)
print(rounded_number)

# Output: 13

print(round(2.665, 2))
print(round(2.676, 2))

from decimal import Decimal

# normal float
num = 2.675
print(round(num, 2))

# using decimal.Decimal (passed float as string for precision)
num = Decimal('2.675')
print(round(num, 2))