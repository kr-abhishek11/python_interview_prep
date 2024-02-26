# example of method overriding
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"Area of the Circle with radius {self.radius} is "+ str(3.14*self.radius*self.radius))

c = Circle(3)
c.area()