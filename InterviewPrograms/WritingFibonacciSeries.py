fib = [0,1]
for i in range(0,5):
    fib.append(fib[-2]+fib[-1])
print(fib)

i = 0
j = 1
k = 0
print(i)
print(j)

# alternate
for l in range(6):
    if k<=13:
        k = i+j
        i = j
        j = k

        print(j)
