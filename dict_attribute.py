class Person:
    salary = 1000
    def __init__(self,name,age):
        self.name = name
        self.age = age

obj = Person("Abhishek",27)
print(obj.__dict__)
print(Person.__dict__)
print(help(obj))