"""
In python there is no strict concept of "private" access modifiers like in other programmming languages. However, a convention
has been established to indicate that a variable or method should be considered private by prefixing its name with a 
__(double underscore)
"""

class MyClass:
    def __init__(self):
        self.__name = "Kumar Abhishek"

a = MyClass()
# print(a.__name) # will throw an error
print(dir(a))
print(a._MyClass__name) # this is called name mangling