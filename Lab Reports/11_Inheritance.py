class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, length, breadth):
        super().__init__(color)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


c1 = Circle("red", 5)
r1 = Rectangle("blue", 12, 10)

print(f"Area of Circle: {c1.area()} sq. units")
print(f"Area of Rectangle: {r1.area()} sq. units")
