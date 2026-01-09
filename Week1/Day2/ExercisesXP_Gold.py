##  Exercise 1: Concatenate lists
# Instructions
# Write code that concatenates two lists together without using the + sign.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

###################################################################################
#############################################################################
##  Exercise 2: Range of numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)

###################################################################################
#############################################################################
##  Exercise 3: Check the index
# Instructions
# Using this variable

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
user_name = input("Enter your name: ")
if user_name in names:
    print(f"Your name is found at index: {names.index(user_name)}")
else:
    print("Your name is not in the list.")

###################################################################################
#############################################################################
##  Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")

###################################################################################
#############################################################################
##  Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
###################################################################################
#############################################################################
#   Exercise 6: Words and letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
words = []
for _ in range(7):
    word = input("Enter a word: ")
    words.append(word)
letter = input("Enter a single character: ")
for word in words:
    if letter in word:
        print(f"In the word '{word}', the letter '{letter}' is found at index: {word.index(letter)}")
    else:
        print(f"The letter '{letter}' is not found in the word '{word}'.")
###################################################################################
#############################################################################
##  Exercise 7: Min, Max, Sum
#Instructions
#Create a list of numbers from one to one million and then use min() 
# and max() to make sure your list actually starts at one and ends at one million. 
# Use the sum() function to see how quickly Python can add a million numbers.
numbers = list(range(1, 1000001))
print(f"Minimum number: {min(numbers)}")
print(f"Maximum number: {max(numbers)}")
print(f"Sum of numbers: {sum(numbers)}")
###################################################################################
#############################################################################
##  Exercise 8 : List and Tuple
# Instructions
#Write a program which accepts a sequence of comma-separated numbers.
#  Generate a list and a tuple which contain every number.
numbers = input("Enter a sequence of comma-separated numbers: ")
number_list = numbers.split(',')
number_tuple = tuple(number_list)
print(f"List: {number_list}")
print(f"Tuple: {number_tuple}") 
###################################################################################
#############################################################################
#   Exercise 9 : Random number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
import random
user_guess = int(input("Guess a number between 1 and 9: "))
random_number = random.randint(1, 9)
if user_guess == random_number:
    print("Winner!")    
else:
    print(f"Better luck next time! The correct number was {random_number}.")
#Bonus: use a loop that allows the user to keep guessing until they want to quit.
while True:
    user_input = input("Guess a number between 1 and 9 (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Thanks for playing!")
        break
    user_guess = int(user_input)
    random_number = random.randint(1, 9)
    if user_guess == random_number:
        print("Winner!")
    else:
        print(f"Better luck next time! The correct number was {random_number}.")
# Bonus 2: on exiting the loop tally up and display total games won and lost.
wins = 0
losses = 0
while True:
    user_input = input("Guess a number between 1 and 9 (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print(f"Thanks for playing! You won {wins} times and lost {losses} times.")
        break
    user_guess = int(user_input)
    random_number = random.randint(1, 9)
    if user_guess == random_number:
        print("Winner!")
        wins += 1
    else:
        print(f"Better luck next time! The correct number was {random_number}.")
        losses += 1
###################################################################################
#############################################################################
