def decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after function")

    return wrapper


@decorator
def greet():
    print("hello")


greet()