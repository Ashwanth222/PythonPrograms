def myGenerator(n):

    value  = 0

    while value <n:
        yield value
        value +=1

for value in myGenerator(5):
    print(value)

#

def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)

#



# generator = my_generator(3)
# print(next(generator))

squares_generator = (i*i for i in range(5))

for i in squares_generator:
    print(i)

    #

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(fibonacci_numbers(3))
print(square(fibonacci_numbers(3)))
print(sum(square(fibonacci_numbers(3))))
# print(sum(square(fibonacci_numbers(4))))

# Output: 4895