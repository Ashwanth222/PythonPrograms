arr1 = [1, 2, 3, 4, 4, 6, 7, 8]

target = 8
flag = 0

for i in range(len(arr1)-1):
    for j in range(len(arr1)-1):
        if arr1[i] + arr1[j] == target and i != j and i > j:
            flag = 1
            print(arr1[i], arr1[j])

if flag == 0:
    print("two sum not equal to target")