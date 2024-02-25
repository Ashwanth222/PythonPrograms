a = "hellehh"
b = ""
l = len(a)-1
i = 0

for i in a:
    b = i + b
print(b)

# alternate
first = 0
last = len(a)-1
mid = (first + last)/2
flag = 0
while first<=mid:
    if (a[first] == a[last]):
       first += 1
       last  -=1
    else:
        flag = 1
        break
if(flag == 0):
    print("is a  palindrome")
else:
    print("is not a paindrome")
