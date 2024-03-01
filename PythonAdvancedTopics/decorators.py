def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)  # prints 11

# Output: 11

# passing function as a argument

def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)  # prints 10

# return function as a value

def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("Atlantis")
print(greet())  # prints "Hello, Atlantis!"

# Output: Hello, Atlantis!

#

def make_pretty(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")

# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()


#

def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()

#

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)

# Chaining Decorators

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")

# The above syntax of,
#
# @star
# @percent
# def printer(msg):
#     print(msg)
# is equivalent to
#
# def printer(msg):
#     print(msg)
# printer = star(percent(printer))
# The order in which we chain decorators matter. If we had reversed the order as,
#
# @percent
# @star
# def printer(msg):
#     print(msg)
# The output would be:
#
# %%%%%%%%%%%%%%%
# ***************
# Hello
# ***************
# %%%%%%%%%%%%%%%

