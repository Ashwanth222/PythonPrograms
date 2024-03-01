def methodName(name,age):
    print('me name is ' + name + ' and my age is ' + str(age))

methodName("nmae", 45)

# def methodName(age):
#     print('  my age is ' + age)
#
# methodName(45)
#
# print('  my age is ' + age)
# TypeError: can only concatenate str (not "int") to str

def methodName(age):
    print('  my age is ', age)

methodName(45)

def addNumbers(num1, num2):
    return num1 +num2

print(addNumbers(34,43))