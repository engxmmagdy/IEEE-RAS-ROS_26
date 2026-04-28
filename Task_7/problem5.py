import math

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, d):
        self.d = d 
    def area(self):
        return self.d*self.d
    
class Circle(Shape):
    def __init__(self, r):
        self.r = r 
    def area(self):
        return math.pi*self.r*self.r
    
square1 = Square(4)
circle1 = Circle(4)

def print_area(shape_obj):
    print(shape_obj.area())

print_area(square1)
print_area(circle1)

        