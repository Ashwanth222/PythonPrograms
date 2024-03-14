numList = [1, 2, 3, 4, 5]

print(numList[((len(numList)-1)/2).__ceil__()])


# alternate
middleElement = int(len(numList)/2)
print(numList[middleElement])