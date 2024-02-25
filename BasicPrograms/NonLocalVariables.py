message = "outside"
def outer():
    message = "outside"

    def inner():
        message = "inside"
        print('inner',message)

    inner()
    print('outer',message)

outer()