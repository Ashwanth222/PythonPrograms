numberList = [15, 85, 35, 89, 125, 566]
max = 1
for i in numberList:
    if max < i:
        max = i

print(max)

#
maxNum = numberList[0]
for num in numberList:
    if maxNum < num:
        maxNum = num
print(maxNum)