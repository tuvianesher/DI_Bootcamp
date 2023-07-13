import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Please specify either the radius or the diameter.")
    
    @property
    def diameter(self):
        return self.radius * 2
    
    def area(self):
        return math.pi * self.radius**2
    
    def __str__(self):
        return f"Circle with radius {self.radius}"
    
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        else:
            raise TypeError("Unsupported operand type for +: 'Circle' and '{}'".format(type(other)))
    
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise TypeError("Unsupported operand type for <: 'Circle' and '{}'".format(type(other)))
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            raise TypeError("Unsupported operand type for ==: 'Circle' and '{}'".format(type(other)))

circles = [Circle(5), Circle(2), Circle(8), Circle(3)]
sorted_circles = sorted(circles)

print(sorted_circles)  # Output: [Circle(radius=2), Circle(radius=3), Circle(radius=5), Circle(radius=8)]

# Bonus: Drawing the sorted circles using Turtle module
import turtle

screen = turtle.Screen()
screen.title("Sorted Circles")
screen.setup(width=800, height=600)
screen.bgcolor("white")

start_x = -200
start_y = 200

turtle.penup()
turtle.goto(start_x, start_y)

for circle in sorted_circles:
    turtle.pendown()
    turtle.circle(circle.radius)
    turtle.penup()
    start_y -= 50
    turtle.goto(start_x, start_y)

turtle.done()
