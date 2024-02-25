global_variable = 10

def outer():
    outer_variable = 20
    print("outer_variable", outer_variable)

    def inner():
        inner_variable = 30
        print("inner_variable", inner_variable)

    inner()

print("global_vaiable", global_variable)
outer()

def myfunction():
    global global_variable
    global_variable = 40
    print('global_variable', global_variable)

myfunction()
