class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang

rohan = Employee("Rohan Das",420)
kumar = Programmer("Kumar Abhishek",1108,"Python")
print(kumar.name)
print(kumar.id)
print(kumar.lang)
