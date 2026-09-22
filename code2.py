# area of rectangle

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def parameter(self):
        return 2 * self.length * self.breadth

obj1 = Rectangle(50,20)
print(obj1.area())
print(obj1.parameter())