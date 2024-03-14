lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

list3 =[]

list3.extend(lst2)
list3.extend(lst1)
print(list3)

# alternate

lst2.extend(lst1)
print(lst2)
