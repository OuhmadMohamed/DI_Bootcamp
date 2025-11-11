# Exercise 1: Cats
class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Step 1: Create Cat Objects
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 5)
cat3 = Cat("Shadow", 2)
#Step 2: Create a Function to Find the Oldest Cat
def oldest_cat(cat_list):
    oldest = cat_list[0]
    for cat in cat_list:
        if cat.age > oldest.age: oldest = cat
    return oldest
#Step 3: Print the Oldest Cat’s Details
cats = [cat1, cat2, cat3]   
oldest = oldest_cat(cats)
print(f"The oldest cat is {oldest.name}, and it is {oldest.age} years old.")

###########################################################
#Exercise 2: Dogs
#STEP 1: Create a Dog Class
class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x=self.height*2
        print(f"{self.name} jumps {x} cm heigh!")
#STEP 2: Create Dog Objects
davids_dog = Dog("BOBI",34)
sarahs_dog = Dog("ZORO",10)
#Step 3: Print Dog Details and Call Methods
davids_dog.bark()
davids_dog.jump()
Dog.bark(sarahs_dog)
Dog.jump(sarahs_dog)
#Step 4: Compare Dog sizes
def bigger_dog(dog1,dog2):
    if dog1.height>dog2.height:
        return dog1
    else:
        return dog2
big_dog=bigger_dog(davids_dog,sarahs_dog)
print(f"The bigger dog is {big_dog.name} with a height of {big_dog.height} cm.")
###########################################################
#Exercise 3: Who’s The Song Producer?
#STEP 1: Create a Song Class
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway=Song(["There's a lady who's sure","all that glitters is gold","and she's buying a stairway to heaven"])
stairway.sing_me_a_song()   
###########################################################
#Exercise 4: Afternoon at the Zoo
#STEP 1: Create a Zoo Class
class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        animal_dict = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter not in animal_dict:
                animal_dict[first_letter] = [animal]
            else:
                animal_dict[first_letter].append(animal)
        return animal_dict

    def get_groups(self):
        sorted_animals = self.sort_animals()
        for key, value in sorted_animals.items():
            print(f"{key}: {value}")
#Step 2: Create a Zoo Object
ramatical_zoo = Zoo("Dramatical Zoo")
#Step 3: Call the Zoo Methods
# Adding Animals
ramatical_zoo.add_animal("Lion")    
ramatical_zoo.add_animal("Tiger")
ramatical_zoo.add_animal("Bear")
ramatical_zoo.add_animal("Giraffe")
ramatical_zoo.add_animal("Zebra")
ramatical_zoo.add_animal("Elephant")
# Getting Animals
print("Animals in the zoo:")    
ramatical_zoo.get_animals()
# Selling an Animal
# Selling the "Bear"
ramatical_zoo.sell_animal("Bear")
print("\nAnimals in the zoo after selling Bear:")    
ramatical_zoo.get_animals()
# Sorting Animals
print("\nSorted animals in the zoo:")
ramatical_zoo.get_groups()
###########################################################   
#Bonus: Modify the add_animal() method to get *args 
#so you dont need to repeat the method each time 
#for a new animal, you can pass multiple animals 
#names separated by a comma.
def add_animal(self, *new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
Zoo.add_animal = add_animal
# Now you can add multiple animals at once
print("\nNew add_animal method with *args:")
ramatical_zoo.add_animal("Panda", "Kangaroo", "Penguin")
print("Animals in the zoo after adding multiple animals:")    
ramatical_zoo.get_animals() 
###########################################################
