
class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width*self.height
    
rectangle_area = rectangle(10,20)
print(rectangle_area.get_area())
        