class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"Employee details are as : ID- {self.id} and Name - {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("Default language is Python")

obj1 = Programmer("Abhishek","1108")
obj1.showDetails()
obj1.showLanguage()