str1 = "Listen"
str2 = "Silent"

str1 = str1.lower()
str2 = str2.lower()

print(str1)
print(str2)

sortedStr1 = sorted(str1)
sortedStr2 = sorted(str2)

print(sortedStr1)
print(sortedStr2)
flag = False
for i in range(0, len(sortedStr1)):
    if sortedStr1[i] != sortedStr2[i]:
        flag = True

if flag :
    print("not anagrams")
else:
    print("are anagrams")


# alternate

str1 = list(str1.lower())
str2 = list(str2.lower())
str1.sort(), str2.sort()

print(str1)
print(str2)

if str1 == str2:
    print("true")
else:
    print("false")



