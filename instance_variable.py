class Employee:
    def __init__(self,name):
        self.name = name #instance variable (defined under the init method and is unique for all the instances of the class)
    def print_name(self):
        print(self.name)

obj1 = Employee("Abhishek")
obj2 = Employee("Harsh")

obj1.print_name()
obj2.print_name()