#🌟 Exercise 1: Favorite Numbers
#Key Python Topics:
#
#Sets
#Adding/removing items in a set
#Set concatenation (using union)
#
#
#Instructions:
#
#Create a set called my_fav_numbers and populate it with your favorite numbers.
my_fav_numbers = {3, 7, 21}
#Add two new numbers to the set.
my_fav_numbers.add(42)
my_fav_numbers.add(99)
#Remove the last number you added to the set.
my_fav_numbers.remove(99)
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
friend_fav_numbers = {5, 12, 21}
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
#Note: Sets are unordered collections, so ensure no duplicate numbers are added.
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)
#############################################################################################################

#🌟 Exercise 2: Tuple
#Key Python Topics:
#
#Tuples (immutability)
#
#
#Instructions:
#
#Given a tuple of integers, try to add more integers to the tuple.
#Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
#
Tuple = (1, 2, 3, 4, 5)
print("Tuples are immutable; you cannot add more integers to a tuple.")
################################################################################################################
#🌟 Exercise 3: List Manipulation
#Key Python Topics:
#
#Lists
#List methods: append, remove, insert, count, clear
#
#
#Instructions:
#
#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
#Remove "Blueberries" from the list.
#Add "Kiwi" to the end of the list.
#Add "Apples" to the beginning of the list.
#Count how many times "Apples" appear in the list.
#Empty the list.
#Print the final state of the list.
#
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
print("Number of times 'Apples' appear in the list:", apple_count)
basket.clear()
print("Final state of the list:", basket)
############################################################################################
#🌟 Exercise 4: Floats
#Key Python Topics:
#
#Lists
#Floats and integers
#Range generation
#
#
#Instructions:
#
#Recap: What is a float? What’s the difference between a float and an integer?
#Create a list containing the following sequence of mixed types: floats and integers:
#1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
#Avoid hard-coding each number manually.
#Think: Can you generate this sequence using a loop or another method?
#
#A float is a number that has a decimal point, while an integer is a whole number without a decimal point.
mixed_numbers = [int(x * 0.5) if (x*0.5).is_integer() else x * 0.5 for x in range(3, 11)]
print("List of mixed floats and integers:", mixed_numbers)

###############################################################################################
#🌟 Exercise 5: For Loop
#Key Python Topics:
#
#Loops (for)
#Range and indexing
#
#
#Instructions:
#
#Write a for loop to print all numbers from 1 to 20, inclusive.
#Write another for loop that prints every number from 1 to 20 where the index is even.
#
#Example:
for number in range(1, 21):
    print(number)
print("Numbers with even indices:")
for index in range(1,21): 
    if index % 2 == 0:
       print(index )

###############################################################################################
#🌟 Exercise 6: While Loop
#Key Python Topics:
#
#Loops (while)
#Conditionals
#
#
#Instructions:
#
#Use an input to ask the user to enter their name.
#Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
#hint: check for the method isdigit()
#if the input is incorrect, keep asking for the correct input until it is correct
#if the input is correct print “thank you” and break the loop
#Example:
#
#Alt text
#
#
name = input("Please enter your name: ")
while True:
    if name.isdigit() or len(name) < 3:
        name = input("Invalid input. Please enter a proper name (at least 3 letters and no digits): ")
    else:
        print("Thank you!")
        break
###############################################################################################
#🌟 Exercise 7: Favorite Fruits
#Key Python Topics:
#
#Input/output
#Strings and lists
#Conditionals
#
#
#Instructions:
#
#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
#Store these fruits in a list.
#Ask the user to input the name of any fruit.
#If the fruit is in their list of favorite fruits, print:
#"You chose one of your favorite fruits! Enjoy!"
#If not, print:
#"You chose a new fruit. I hope you enjoy it!"
#
favorite_fruits = input("Please enter your favorite fruits (separated by spaces): ").split()
fruit_choice = input("Please enter the name of any fruit: ")
if fruit_choice in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

##############################################################################################
#🌟 Exercise 8: Pizza Toppings
#Key Python Topics:
#
#Loops
#Lists
#String formatting
#
#
#Instructions:
#
#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types 'quit'.
#For each topping entered, print:
#"Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.
#
toppings = []
while True: 
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")
base_price = 10
topping_price = 2.5 * len(toppings)
total_price = base_price + topping_price
print("Your pizza toppings:", ", ".join(toppings))
print(f"Total cost of the pizza: ${total_price:.2f}")

##############################################################################################
#🌟 Exercise 9: Cinemax Tickets
#Key Python Topics:
#
#Conditionals
#Lists
#Loops
#
#
#Instructions:
#
#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
#Free for people under 3.
#$10 for people aged 3 to 12.
#$15 for anyone over 12.
#Print the total ticket cost.
#
#

total_cost = 0
while True:
    age = input("Enter the age of the family member (or type 'done' to finish): ")
    if age.lower() == 'done':
        break
    age = int(age)
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost
print(f"Total ticket cost for the family: ${total_cost}")

#Bonus:
#
#Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
#Write a program to:
#Ask for each person’s age.
#Remove anyone who isn’t allowed to watch.
#Print the final list of attendees.
#
teenagers = []
while True:
    age_input = input("Enter the age of the teenager (or type 'done' to finish): ")
    if age_input.lower() == 'done':
        break
    age = int(age_input)
    if 16 <= age <= 21:
        teenagers.append(age)   
print("Final list of attendees allowed to watch the movie:", teenagers)

##############################################################################################