import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


r = float(input("Enter the radius: "))

c = Circle(r)

print("Area of Circle =", round(c.area(), 2))
print("Perimeter of Circle =", round(c.perimeter(), 2))
