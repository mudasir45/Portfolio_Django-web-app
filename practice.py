class Shape:
    def area(self):
        print("Area of shape: ?")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# shapes = [Circle(5), Rectangle(4, 6)]

# for shape in shapes:
#     print(f"Area of shape: {shape.area()}")
r = Rectangle(5)
r.area()