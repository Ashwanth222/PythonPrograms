arr = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0
temp = 0
while i < len(arr):
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp
    i += 2

print(arr)


