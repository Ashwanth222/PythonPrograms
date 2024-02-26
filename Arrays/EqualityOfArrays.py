arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = [1, 2, 3, 4, 4, 6, 7, 8]

# inbuilt
t = arr1.__eq__(arr2)

# alternate
print(t)
l = len(arr2)-1
i = 0
flag = 1

if len(arr2) == len(arr1):
    while l >=0:
        if arr1[i] != arr2[i]:
            flag = 0
            break
        else:
            i +=1
            l -=1
else:
    flag = 0
if flag:
    print(" equal")
else:
    print("arrays not equal")





