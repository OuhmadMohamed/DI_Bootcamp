# Challenge 1: Multiples of a Number
# Ask the user for inputs
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

# Create an empty list to store multiples
multiples = []

# Generate multiples using a loop
for i in range(1, length + 1):
    multiples.append(number * i)

# Print the result
print(multiples)


##################################################################
##################################################################
# Challenge 2: Remove Consecutive Duplicate Letters
# Ask the user for a string
word = input("Enter a word: ")

# Variable to store the result
result = ""

# Loop through the characters of the string
for char in word:
    # Add the character only if it's not the same as the previous one
    if len(result) == 0 or char != result[-1]:
        result += char

# Print the final cleaned string
print("Output:", result)
