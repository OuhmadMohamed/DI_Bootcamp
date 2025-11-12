#Exercises 3: Dogs Domesticated
#Step 1: Import the Dog Class
from ExercisesXP import Dog
#Step 2: Create the PetDog Class
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.trained = True
        print(self.bark())

    def play(self, *args):
        dog_names = ', '.join([itm_in_args.name for itm_in_args in args])
        print(f"{dog_names} all playing together")

    def do_a_trick(self):
        import random
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained:
            print(f"{self.name} {random.choice(tricks)}")
    
#Step 4: Test PetDog Methods
#Create PetDog Instances
pet_dog1 = PetDog("Charlie", 4, 30)
pet_dog2 = PetDog("Cooper", 2, 20)
pet_dog3 = PetDog("Duke", 5, 25)
#Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.
pet_dog1.train()
pet_dog1.play(pet_dog2, pet_dog3)   
pet_dog1.do_a_trick()
#Exercise 4: Family and Person Classes
#Step 1: Create the Person Class
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.last_name = ' '
        self.age = age
    def is_18(self):
        return self.age >= 18
#Step 2: Create the Family Class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_member = Person (first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"{first_name} You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print(f"{first_name} Sorry, you are not allowed to go out with your friends.")
    def family_presentation(self):
        print(f'{self.last_name} Family Members:')
        for member in self.members:
            print(f'{member.first_name}, Age: {member.age}')
#Step 3: Test the Family and Person Classes
Family_name = Family("Johnson")
Family_name.born("Jane", 45)
Family_name.born("John", 50)
Family_name.born("Alice", 17)
Family_name.born("Bob", 20)
Family_name.check_majority("Alice")
Family_name.check_majority("Bob")
Family_name.family_presentation()

