arr1 = [1, 2, 3, 4, 4, 6, 7, 8]
arr1.reverse()
print(arr1)

arr1.pop(4)
print(arr1)

arr1.remove(6)
print(arr1)

arr1.append(7)
print(arr1)

arr3 =arr1.copy()
print(arr3)

c = arr3.count(4)
print(c)

arr3.extend(arr1)
print(arr3)

print(arr3.__sizeof__())



