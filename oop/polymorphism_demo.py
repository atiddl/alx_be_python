import math

class Shape:
    """Base class for shapes. Subclasses must implement the area method."""
    def area(self):
        """Method to calculate the area. Must be overridden in subclasses."""
        raise NotImplementedError("Subclasses must override this method")

class Rectangle(Shape):
    """Rectangle shape with length and width."""
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Circle shape with radius."""
    def __init__(self, radius):
        """Initialize the circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)