"""
Multiple Inheritance - OOPs feature that allows a child class to inherit functionalities from multiple parent classes.
This can be useful in situations where a class needs to inherit functionality from multiple sources.
--> It is important to note that, in case of multiple inheritance, Python follows a Method Resolution Order- MRO
to resolve conflicts between methods/attributes from different parent classes. The MRO determines the order in which parent
classes are searched for attributes and methods.
"""
class Employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Dancer,Employee):
    def __init__(self,name,dance):
        self.name = name
        self.dance = dance
        
obj = DancerEmployee("Harsh","Hip-Hop")
print(obj.name)
print(obj.dance)
obj.show()
print(DancerEmployee.mro())
