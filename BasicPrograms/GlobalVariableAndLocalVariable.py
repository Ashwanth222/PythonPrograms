message = "hello"

def greet():
    print("local", message)


greet()
print('global', message)