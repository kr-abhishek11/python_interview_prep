class Person:
    name = "Kumar Abhishek"
    occupation = "Software Developer"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person() # a is an object of person class
# self is a keyword that initiates class constructor
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
a.name = "Harsh Vardhan"
a.occupation= "Blockchain developer"
print(a.info())