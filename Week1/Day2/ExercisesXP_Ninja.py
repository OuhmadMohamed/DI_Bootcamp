##  Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
import math
C = 50
H = 30
user_input = input("Enter comma-separated numbers: ")
D_values = user_input.split(',')
results = []
for D in D_values:
    Q = math.sqrt((2 * C * int(D)) / H)
    results.append(str(round(Q)))
print(','.join(results))
###################################################################################
#############################################################################
##  Exercise 2 : List of integers
# Instructions
# Given a list of 10 integers to analyze. 
# 1. Store the list of numbers in a variable.
numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

#The list of numbers – printed in a single line, separated by commas.
print("Numbers:", ','.join(map(str, numbers)))
#he list of numbers – sorted in descending order (largest to smallest)
sorted_numbers = sorted(numbers, reverse=True)
print("Sorted (descending):", ','.join(map(str, sorted_numbers)))
#the sum of all the numbers in the list.
total_sum = sum(numbers)   
print("Sum of numbers:", total_sum)

#3. A list containing the first and the last numbers.
first_last = [numbers[0], numbers[-1]]
print("First and last numbers:", first_last)

#4. A list of all the numbers greater than 50.
greater_than_50 = [num for num in numbers if num > 50]
print("Numbers greater than 50:", greater_than_50)

#5. A list of all the numbers smaller than 10.
smaller_than_10 = [num for num in numbers if num < 10]
print("Numbers smaller than 10:", smaller_than_10)

#6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
squared_numbers = [num ** 2 for num in numbers]
print("Squared numbers:", squared_numbers)

#7. The numbers without any duplicates – also print how many numbers are in the new list.
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)

#8. The average of all the numbers.
average = total_sum / len(numbers)
print("Average of numbers:", average)

#9. The largest number.
greatest = max(numbers)
print(f"The greatest number is: {greatest}")

#10.The smallest number.
smallest = min(numbers)
print(f"The smallest number is: {smallest}")

#11. Bonus: Find the sum, average, largest and smallest number without using built in functions.
manual_sum = 0
i=0
manual_largest = numbers[0]
manual_smallest = numbers[0]
for num in numbers:
    manual_sum += num
    i+=1
    if num > manual_largest:
        manual_largest = num
    if num < manual_smallest:
        manual_smallest = num
manual_average = manual_sum / i
print("Manual Sum:", manual_sum)
print("Manual Average:", manual_average)
print("Manual Largest:", manual_largest)
print("Manual Smallest:", manual_smallest)

# 12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
user_numbers = []
while len(user_numbers) < 10:
    user_input = int(input("Enter an integer between -100 and 100: "))
    if -100 <= user_input <= 100:
        user_numbers.append(user_input)
    else:
        print("Number out of range, please try again.")
print("User entered numbers:", user_numbers)

# 13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
import random
print("Randomly generated numbers:", random_numbers)

#14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
import random
amount = random.randint(50, 100)
random_numbers_variable = [random.randint(-100, 100) for i in range(amount)]
print(f"Randomly generated {amount} numbers:", random_numbers_variable)

#15. Bonus: Will the code work when the number of random numbers is not equal to 10?
# Yes, the code will work as it dynamically handles the length of the list.

###################################################################################
#############################################################################
##  Exercise 3: Working on a paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
paragraph = """Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."""
# Number of characters
num_characters = len(paragraph)
print(f"Number of characters: {num_characters}")
# Number of sentences
num_sentences = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')
print(f"Number of sentences: {num_sentences}")
# Number of words
words = paragraph.split()
num_words = len(words)
print(f"Number of words: {num_words}")
# Number of unique words
unique_words = set(words)
num_unique_words = len(unique_words) 
print(f"Number of unique words: {num_unique_words}")

#Bonus: How many non-whitespace characters it contains.
num_non_whitespace = len(paragraph.replace(" ", "").replace("\n", ""))
print(f"Number of non-whitespace characters: {num_non_whitespace}")

#Bonus: The average amount of words per sentence in the paragraph.
average_words_per_sentence = num_words / num_sentences if num_sentences > 0 else 0
print(f"Average words per sentence: {average_words_per_sentence}")

# Bonus: the amount of non-unique words in the paragraph.
num_non_unique_words = num_words - num_unique_words
print(f"Number of non-unique words: {num_non_unique_words}")

###################################################################################
#############################################################################
