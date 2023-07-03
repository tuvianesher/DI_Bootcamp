import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def print_definition(self):
        print("A circle is a closed curve where all points are equidistant from the center.")

# Create an instance of the Circle class
circle = Circle(3.5)

# Compute and print the perimeter
perimeter = circle.perimeter()
print(f"The perimeter of the circle is: {perimeter}")

# Compute and print the area
area = circle.area()
print(f"The area of the circle is: {area}")

# Print the geometrical definition of a circle
circle.print_definition()
