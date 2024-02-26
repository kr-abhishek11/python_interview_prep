class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def make_sound(self):
        print(f"Sound made by {self.name} of {self.species} - ")

class Dog(Animal):
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def make_sound(self):
        print(f"Dog named {self.name} of {self.breed} breed barks")

dog1 = Dog("Bruno","Doberman")
dog1.make_sound()
animal1 = Animal("Horsey","Horse")
animal1.make_sound()    