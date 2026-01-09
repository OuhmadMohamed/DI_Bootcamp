###    Daily Challenge: Dictionaries
## Challenge 1: Letter Index Dictionary 
# Goal: Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).
# Ask user for a word
word = input("Enter a word: ").lower()

# Create an empty dictionary
letter_index_dict = {}

# Loop through each character with its index
for index, char in enumerate(word):
    if char in letter_index_dict:
        # If key exists, append index
        letter_index_dict[char].append(index)
    else:
        # Otherwise create a new key with a list containing the index
        letter_index_dict[char] = [index]

# Print the result
print(letter_index_dict)

######################################################
###########################################################
# Challenge 2: Affordable Items
# Goal: Create a program that prints a list of items that can be purchased with a given amount of money.

# Given data
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Step 1: Clean the wallet value
wallet = int(wallet.replace("$", "").replace(",", ""))

# Create empty basket
basket = []

# Step 2: Loop through items in order of priority (dictionary order)
for item, price in items_purchase.items():
    # Clean the price string
    clean_price = int(price.replace("$", "").replace(",", ""))

    # Check if the item can be afforded
    if wallet >= clean_price:
        basket.append(item)
        wallet -= clean_price  # update wallet

# Step 3: Print result
if not basket:
    print("Nothing")
else:
    print(sorted(basket))
