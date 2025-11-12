#🌟 Exercise 1: Pets

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is walking"    
class Bengal(Cat):
    pass    
class Chartreux(Cat):
    pass    
# Step 1: Create the Siamese Class
class Siamese(Cat):
    pass
# Step 2: Create a List of Cat Instances
all_cats = [ Bengal("Leo", 3),    Chartreux("Milo", 4),    Siamese("Luna", 2)]
# Step 3: Create a Pets Instance    
class Pets:
    def __init__(self, cats):
        self.cats = cats

    def walk(self):
        for cat in self.cats:
            print(cat.walk())   
sara_pets = Pets(all_cats)
# Step 4: Take Cats for a Walk
#sara_pets.walk()
################################################
#Exercises 2: Dogs
#Step 1: Create the Dog Class
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} wins the fight against {other_dog.name}"
        else:
            return f"{other_dog.name} wins the fight against {self.name}"

#Step 2: Create Dog Instances
dog1 = Dog("Buddy", 5, 20)
dog2 = Dog("Max", 3, 15)
dog3 = Dog("Rocky", 4, 25)

#Step 3: Test Dog Methods
#print(dog1.bark())
#print(dog2.run_speed())
#print(dog1.fight(dog2))

