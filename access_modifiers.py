class Employee:
    def __init__(self):
        self.__name = "Kumar Abhishek"

obj = Employee()
print(obj._Employee__name)
print(obj.__dir__())