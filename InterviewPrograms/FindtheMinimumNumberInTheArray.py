numberList = [15, 85, 35, 89, 125, 566, 10]

min = numberList[0]

for i in numberList:
    if min > i:
        min = i

print(min)