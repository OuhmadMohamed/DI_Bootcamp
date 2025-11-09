#Exercise 1 : Use the terminal
#Instructions
#Run this command in the terminal to open a python console:
#$ python3
#Hint: Replace python3 with python for Windows

#Read about the PATH variable. Try to explain why you can call python3 if you aren’t in the executable directory.
print("The PATH variable is a list of directories your system searches through to find and run programs without needing their full paths. So when you type a command (like python) in the terminal, your system goes through all the folders in PATH and looks for an executable file named as python.exe.")
      
###########################################################################
#Exercise 2 : Alias
#Instructions
#Read about alias, and try to open a python console with the command:
#
#$ py
#

##########################################################################
#Exercise 3 : Outputs
#Instructions
#Predict the output of the following code snippets:
#
#    >>> 3 <= 3 < 9                       # True 
#    >>> 3 == 3 == 3                      # True
#    >>> bool(0)                          # False
#    >>> bool(5 == "5")                   # False
#    >>> bool(4 == 4) == bool("4" == "4") # True
#    >>> bool(bool(None))                 # False
x = (1 == True)                      # True
y = (1 == False)                     # False
a = True + 4                         # 5
b = False + 10                       # 10

print("x is", x)                     # x is True
print("y is", y)                     # y is False 
print("a:", a)                       # a: 5
print("b:", b)                       # b: 10

#######################################################################
#Exercise 4 : How many characters in a sentence ?
#Instructions
#Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
#
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print("number of characters in my text",len(my_text))
###########################################
#Exercise 5: Longest word without a specific character
#Instructions
#Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.
longest_sentence = ""
while True:
    sentence = input("Please enter the longest sentence you can without the character 'A' (or type 'exit' to quit): ")
    if sentence.lower() == 'exit':
        break
    if 'A' in sentence.upper():
        print("Your sentence contains the character 'A'. Please try again.")
    else:
        if len(sentence) > len(longest_sentence):
            longest_sentence = sentence
            print("Congratulations! You've set a new longest sentence!")
        else:
            print("Your sentence is valid but not the longest yet. Keep trying!")   
print("The longest sentence without 'A' is:", longest_sentence)
###########################################
