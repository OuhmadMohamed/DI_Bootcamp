#----------------------------------------------------
# Exercise 1 : Geometry
#----------------------------------------------------
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def definition(self):
        print("A circle is a set of points in a plane that are at a given distance (radius) from a fixed point (center).")

# Example usage:
c = Circle(5)
print("Perimeter:", c.perimeter())
print("Area:", c.area())
c.definition()

#######################################################################
########################################################################

#---------------------------------------------------------
# Exercise 2: Custom List Class – MyList
#---------------------------------------------------------
import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reversed_list(self):
        return self.letters[::-1]

    def sorted_list(self):
        return sorted(self.letters)

    # Bonus: list of random numbers with same length
    def random_number_list(self):
        return [random.randint(0, 100) for _ in range(len(self.letters))]


# Example
ml = MyList(['d', 'a', 'c', 'b'])
print("Reversed:", ml.reversed_list())
print("Sorted:", ml.sorted_list())
print("Random numbers:", ml.random_number_list())


############################################################
############################################################

#----------------------------------------------------
# Exercise 3: Restaurant Menu Manager
#----------------------------------------------------
from menu_manager import MenuManager

m = MenuManager()
m.add_item("Pizza", 22, "A", True)
m.update_item("Soup", 12, "B", False)
m.remove_item("Salad")
