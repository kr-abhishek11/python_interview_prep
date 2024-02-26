class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromString(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    
e1 = Employee("Abhishek",45000)
print(e1.name)
print(e1.salary)

string = "Abhishek-45000"
e2 = Employee.fromString(string)
print(e2.name)
print(e2.salary)
