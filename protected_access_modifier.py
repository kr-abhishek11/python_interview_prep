"""
In python, the syntax we follow to make any variable protected is to write variable name followed by a single underscore(_) i.e. _varName
Python does not do name mangling for protected variables or methods
Protected members can only be accessed within the class and by its sub classes
"""

class Student:
    def __init__(self):
        self._name = "Kumar Abhishek"

    def _funName(self):
        return "CodeWithKumar"

class Subject(Student):
    pass

obj1 = Student()
obj2 = Subject()
print(obj1._name)
print(obj1._funName())
print(obj2._name)
print(obj2._funName())