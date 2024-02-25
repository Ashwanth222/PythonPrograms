from functools import reduce

arr = [1, 2, 3, 6]
summ = 0
for i in arr:
    summ += i
print(summ)

# alternate
Sum = 0
Sum = sum(arr)
print(Sum)

# alternate
summm = reduce(lambda a,b:a+b,arr)
print(summm)

