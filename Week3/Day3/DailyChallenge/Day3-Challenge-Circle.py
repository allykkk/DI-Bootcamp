import math


class Circle():
    def __init__(self, radius=None, diameter=None):
        # prevent possible bad parameters passing to the obeject, such as -> circle1=Circle(radius=1,diameter=5)
        if radius is not None and diameter is not None:
            raise ValueError("Please provide either the radius or the diameter.")
        elif radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Please provide either the radius or the diameter.")

    # Compute the circle’s area
    def cal_area(self):
        return math.pi * self.radius ** 2

    # Print the circle and get something nice
    def __str__(self):
        return f"Circle with radius: {self.radius}"

    # Be able to put them in a list and sort them
    def __repr__(self):
        return f"Circle({self.radius})"

    # Be able to add two circles together
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        else:
            raise TypeError("Please pass the same object type.")

    # Be able to compare two circles to see which is bigger
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        else:
            raise TypeError("Please pass the same object type.")

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise TypeError("Please pass the same object type.")

    # Be able to compare two circles and see if there are equal
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            return False


circles = [Circle(3), Circle(1), Circle(2)]
circles.sort()
print(circles)
# circle1=Circle(radius=1,diameter=5)
circle2 = Circle(5)
print(circle2.cal_area())
