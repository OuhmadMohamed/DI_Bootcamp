import math

class Circle:
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self._radius = radius

    # -----------------------------
    # Radius (getter & setter)
    # -----------------------------
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # -----------------------------
    # Diameter (computed property)
    # -----------------------------
    @property
    def diameter(self):
        return 2 * self._radius

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Diameter must be positive")
        self._radius = value / 2

    # -----------------------------
    # Area computation
    # -----------------------------
    def area(self):
        return math.pi * self._radius ** 2

    # -----------------------------
    # String representation
    # -----------------------------
    def __str__(self):
        return f"Circle(radius={self._radius:.2f})"

    def __repr__(self):
        return f"Circle(radius={self._radius})"

    # -----------------------------
    # Add two circles
    # -----------------------------
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self._radius + other._radius)

    # -----------------------------
    # Comparisons
    # -----------------------------
    # Compare two circles to check if they are equal
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius == other._radius

    # Compare two circles to see which is bigger
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius > other._radius

    # Store multiple circles in a list and sort them
    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius


#___________________________Example Usage____________________________________#
c1 = Circle(radius=3)
c2 = Circle(radius=5)

print(c1.area())
print(c1.diameter)

c3 = c1 + c2
print(c3)

print(c1 > c2)
print(c1 == c2)

circles = [c2, c1, c3]
circles.sort()
print(circles)
