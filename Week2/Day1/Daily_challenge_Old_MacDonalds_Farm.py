#Daily challenge: Old MacDonald’s Farm
#Step 1: Create the Farm Class
class Farm():
    #Step 2: Implement the __init__ Method
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}
    #Step 3: Implement the add_animal Method
    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
    #Step 4: Implement the get_info Method
    def get_info(self):
        info = f"Farm name: {self.name}\n"
        info += "Animals:\n"
        for animal, count in self.animals.items():
            info += f"{animal:<10} : {count}\n"
        info += "E-I-E-I-0!"
        return info
#Step 5: Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
#macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

#############################################
#Bonus: Expand The Farm
#Step 6: Implement the get_animal_types Method
def get_animal_types(self):
    return sorted(self.animals.keys())
Farm.get_animal_types = get_animal_types
print(macdonald.get_animal_types())
#Step 7: Implement the get_short_info Method
def get_short_info(self):
    animal_types = self.get_animal_types() #call the get_animal_types method to get the sorted animals list
    animal_list = []
    for animal in animal_types:
        if self.animals[animal] > 1:
            animal_list.append(animal + 's')
        else:
            animal_list.append(animal)
    if len(animal_list) > 1:
        last_animal = animal_list.pop()
        animal_str = ', '.join(animal_list) + ' and ' + last_animal
    else:
        animal_str = animal_list[0]
    return f"{self.name}'s farm has {animal_str}."
Farm.get_short_info = get_short_info
print(macdonald.get_short_info())   
#Step 8: upgrade the add_animal Method
def add_animal(self, **animals):
    for animal_type, count in animals.items():
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

Farm.add_animal = add_animal
macdonald.add_animal(cow=3, pig=2, chicken=7, sheep=4)
print(macdonald.get_info())
print(macdonald.get_short_info())
