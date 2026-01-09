# Exercise 1: Birthday Look-up

# Create a dictionary with 5 birthdays
birthdays = {
    "Alice": "1998/04/12",
    "Bob": "2000/11/23",
    "Charlie": "1995/06/30",
    "Dina": "2002/01/15",
    "Elias": "1999/09/05"
}

print("🎉 Welcome to the Birthday Look-up Program! 🎉")
print("You can look up the birthdays of the people in the list!\n")

# Ask the user for a name
name = input("Enter a person's name: ")

# Retrieve the birthday
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print("Sorry, this name is not in the list.")





###########################################################
###########################################################
# Exercise 2: Birthdays Advanced

# Dictionary of birthdays
birthdays = {
    "Alice": "1998/04/12",
    "Bob": "2000/11/23",
    "Charlie": "1995/06/30",
    "Dina": "2002/01/15",
    "Elias": "1999/09/05"
}

print("🎉 Welcome to the Birthday Look-up Program! 🎉")
print("Here are the people in the list:")

# Print all names in the dictionary
for name in birthdays:
    print("-", name)

print()  # Empty line for clarity

# Ask user for a name
person = input("Whose birthday would you like to look up? ")

# Check if name exists
if person in birthdays:
    print(f"{person}'s birthday is on {birthdays[person]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {person}.")




#################################################################################
###############################################################################

##  Exercise 3: Add Your Own Birthday
# Initial dictionary of birthdays
birthdays = {
    "Alice": "1998/04/12",
    "Bob": "2000/11/23",
    "Charlie": "1995/06/30",
    "Dina": "2002/01/15",
    "Elias": "1999/09/05"
}

print("Welcome to the Birthday Look-up Program! 🎉")

# --- Step 1: Ask user to add a new birthday ---
new_name = input("Add a new person's name: ")
new_birthday = input(f"Enter {new_name}'s birthday (YYYY/MM/DD): ")

# Add new entry to dictionary
birthdays[new_name] = new_birthday
print(f"{new_name}'s birthday has been added!\n")

# --- Step 2: Display all names ---
print("Here are all the people in the list:")
for person in birthdays:
    print("-", person)

print()  # Just for spacing

# --- Step 3: Ask user whose birthday they want to look up ---
lookup = input("Whose birthday would you like to look up? ")

# --- Step 4: Check and print ---
if lookup in birthdays:
    print(f"{lookup}'s birthday is on {birthdays[lookup]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {lookup}.")




###########################################################################
############################################################################
##  Exercise 4: Fruit Shop
##  Partie 1 : Afficher les items et leurs prix
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print("📌 List of items and their prices:")

for fruit, price in items.items():
    print(f"The price of {fruit} is {price} DH.")


##  Partie 2 : Calculer le coût total de tout le stock

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_cost = 0

for fruit, data in items.items():
    item_total = data["price"] * data["stock"]
    total_cost += item_total
    print(f"{fruit.capitalize()} → price: {data['price']} DH, stock: {data['stock']}, subtotal: {item_total} DH")

print("\n💰 The total cost to buy everything in stock is:", total_cost, "DH")

