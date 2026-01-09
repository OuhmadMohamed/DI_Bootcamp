##  Timed Challenge #1
# 
# Count occurence
# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.
#

text = input("Enter a string: ").lower()
char = input("Enter a character to count: ").lower()

count = text.count(char)

print("Number of occurrences:", count)
