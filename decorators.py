def greet(func):
    def modified_func():
        print("Good Morning")
        func()
        print("Thanks for using the function")
    return modified_func

@greet
def sample():
    print("Kumar Abhishek")

sample()