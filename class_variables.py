"""
In python, variables can be defined at the class level or at the instance level.
Class varibles are defined at the class level and are shared among all the instances of the class.
They are defined outside of any method and are usually used to store information that is common to all instances of the class
"""

class MyClass:
    no_of_objects = 0 #class variable
    def __init__(self):
        print("Object created")
        MyClass.no_of_objects += 1
    def total_objects(self):
        print(f"Number of total objects created is {MyClass.no_of_objects}")

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
obj3.total_objects()