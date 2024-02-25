import operator
from functools import reduce

arr = [10, 324, 45, 90, 9808, 9999]
max = 0
i = 0
while i< len(arr):
    if arr[i] >max:
        max = arr[i]
        i+=1
    else:
        i+=1
print(max)

# alternate
maxx = arr[0]
for i in range(1,len(arr)):
    if arr[i]>maxx :
        maxx = arr[i]

print(maxx)

# alternate
arr.sort(reverse=True)
print(arr[0])
print(arr.__getitem__(0))








