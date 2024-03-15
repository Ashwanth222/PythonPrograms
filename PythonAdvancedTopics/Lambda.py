s = "this is python"
upper = lambda string: string.upper()
print(upper(s))

st = "this is a python"
lower = lambda string: string.lower()
print(lower(st))

#
format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))

# Difference Between Lambda functions and def defined function

def cube(y):
    return y*y*y

lambda_cube = lambda x: x*x*x
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))

# Python Lambda Function with List Comprehension

is_even_list = [lambda arg=y: arg*10 for y in range(1,5)]
for item in is_even_list:
    print(item())

# Python Lambda Function with if-else

max = lambda a, b : a if a>b else b
print(max(4,8))
print(max(8,4))

#
List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]
sorted_list = lambda x: (sorted(i) for i in List)
second_largest = lambda x, f: [y[len(y)-2] for y in f(x)]
print(second_largest(List, sorted_list))

# print even numbers in list
list1 = [5,7,9,2,4,8,6]
even_numbers = lambda x: [x if x%2 == 0 else None for x in list1]
print(even_numbers(list1))

# Using lambda() Function with filter()
# print odd numbers
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
finalList = list(filter(lambda x: (x%2 != 0),li))
print(finalList)

ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda x: x > 18, ages))
print(adults)

# using lambda() function with map()

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
double = list(map(lambda x: 2*x, li))
print(double)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
square = list(map(lambda x: x*x, li))
print(square)

animals = ['dog', 'cat', 'parrot', 'rabbit']
upper_case = list(map(lambda x: x.upper(), animals))
print(upper_case)

animals = ['DOG', 'CAT', 'PARROT', 'RABBIT']
lower_case = list(map(lambda x: x.lower(), animals))
print(lower_case)

# Using lambda() Function with reduce()
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
summ = reduce((lambda x, y: x+y), li)
print(summ)

# Find the maximum element in a list using lambda and reduce() function
lis = [1, 3, 5, 6, 2, ]
maxx = reduce(lambda x, y:x if x>y else y, lis)
print(maxx)

#


