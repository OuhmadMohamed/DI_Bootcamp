#***********************  Challenges  *****************************
#___________________________________________________________________


#-------------------------------------------------------
# Exercise 1: Insert an item at a defined index in a list
#-------------------------------------------------------

# Function to insert an item at a given index
def insert_item(lst, index, item):
    lst.insert(index, item)
    return lst

# Example usage
my_list = [1, 2, 3, 4]
new_list = insert_item(my_list, 2, 99)  # Insert 99 at index 2
print(new_list)  # Output: [1, 2, 99, 3, 4]

#############################################################
########################################################
#--------------------------------------------------------
# Exercise 2: Count the number of spaces in a string
#----------------------------------------------------------

def count_spaces(text):
    count = 0
    for char in text:
        if char == ' ':
            count += 1
    return count

# Example usage
text = "Hello world, how are you?"
print(count_spaces(text))  # Output: 5

####################################################################
######################################################################
#-------------------------------------------------------------------
#  Exercise 3: Count uppercase and lowercase letters in a string
#----------------------------------------------------------------
def count_letters(text):
    upper_count = 0
    lower_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Example usage
text = "Hello World!"
upper, lower = count_letters(text)
print("Uppercase letters:", upper)  # Output: 2
print("Lowercase letters:", lower)  # Output: 8

####################################################################
##################################################################
#---------------------------------------------------------------
#  Exercise 4: Sum of an array without using sum()
#----------------------------------------------------------------
def my_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Example usage
numbers = [1, 5, 4, 2]
print(my_sum(numbers))  # Output: 12

##########################################################################
########################################################################
#-----------------------------------------------------------------
#  Exercise 5: Find the max number in a list
#-----------------------------------------------------------------
def find_max(lst):
    if not lst:  # Handle empty list
        return None
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

# Example usage
print(find_max([0, 1, 3, 50]))  # Output: 50

#####################################################################
#####################################################################
#---------------------------------------------------------------
#  Exercise 6: Factorial of a number
#------------------------------------------------------------------
def factorial(n):
    if n < 0:
        return None  # Factorial is undefined for negative numbers
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
print(factorial(4))  # Output: 24

####################################################################
###################################################################
#-------------------------------------------------------------------------
#  Exercise 7: Count an element in a list (without count)
#------------------------------------------------------------------------
def list_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage
print(list_count(['a','a','t','o'], 'a'))  # Output: 2

#########################################################################
########################################################################
#-------------------------------------------------------------------
Exercise 8: L2-norm of a list (square root of sum of squares)
#--------------------------------------------------------------------
import math

def norm(lst):
    total = 0
    for num in lst:
        total += num ** 2
    return math.sqrt(total)

# Example usage
print(norm([1, 2, 2]))  # Output: 3.0

###########################################################################
#########################################################################
#---------------------------------------------------------------------
#  Exercise 9: Check if an array is monotonic
#---------------------------------------------------------------------
def is_mono(arr):
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        return True
    if all(arr[i] >= arr[i+1] for i in range(len(arr)-1)):
        return True
    return False

# Example usage
print(is_mono([7,6,5,5,2,0]))  # Output: True
print(is_mono([2,3,3,3]))      # Output: True
print(is_mono([1,2,0,4]))      # Output: False

##############################################################################
#############################################################################
#--------------------------------------------------------------------------
#  Exercise 10: Print the longest word in a list
#-----------------------------------------------------------------------------
def longest_word(words):
    if not words:
        return None
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Example usage
words_list = ["apple", "banana", "cherry", "watermelon"]
print(longest_word(words_list))  # Output: watermelon

###########################################################################
#############################################################################
#------------------------------------------------------------------------
#  Exercise 11: Separate integers and strings in a list
#------------------------------------------------------------------------
def separate_types(lst):
    integers = []
    strings = []
    for item in lst:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, str):
            strings.append(item)
    return integers, strings

# Example usage
mixed_list = [1, "apple", 2, "banana", 3, "cherry"]
ints, strs = separate_types(mixed_list)
print("Integers:", ints)  # Output: [1, 2, 3]
print("Strings:", strs)   # Output: ['apple', 'banana', 'cherry']

##################################################################################
###################################################################################
#-------------------------------------------------------------------------------
#  Exercise 12: Check if a string is a palindrome
#----------------------------------------------------------------------------
def is_palindrome(text):
    return text == text[::-1]

# Example usage
print(is_palindrome('radar'))  # Output: True
print(is_palindrome('John'))   # Output: False

####################################################################################
####################################################################################
#--------------------------------------------------------------------------------
#  Exercise 13: Count words in a sentence with length > k
#---------------------------------------------------------------------------------
def sum_over_k(sentence, k):
    words = sentence.split()
    count = 0
    for word in words:
        if len(word) > k:
            count += 1
    return count

# Example usage
sentence = 'Do or do not there is no try'
k = 2
print(sum_over_k(sentence, k))  # Output: 3

####################################################################################
####################################################################################
#----------------------------------------------------------------------------------
#  Exercise 14: Average value in a dictionary
#-----------------------------------------------------------------------------------
def dict_avg(d):
    if not d:  # Handle empty dictionary
        return 0
    total = 0
    for value in d.values():
        total += value
    return total / len(d)

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 8, 'd': 1}
print(dict_avg(my_dict))  # Output: 3.0

#################################################################################
###################################################################################
#--------------------------------------------------------------------------
#  Exercise 15: Common divisors of 2 numbers
#-----------------------------------------------------------------------------
def common_div(a, b):
    divisors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    return divisors

# Example usage
print(common_div(10, 20))  # Output: [1, 2, 5, 10]

#####################################################################################
####################################################################################
#---------------------------------------------------------------------
#  Exercise 16: Check if a number is prime
#----------------------------------------------------------------------
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(11))  # Output: True
print(is_prime(12))  # Output: False

##############################################################################
#####################################################################################
#---------------------------------------------------------------------------
#  Exercise 17: Print elements if both index and value are even
#----------------------------------------------------------------------------
def weird_print(lst):
    result = [value for index, value in enumerate(lst) if index % 2 == 0 and value % 2 == 0]
    return result

# Example usage
print(weird_print([1, 2, 2, 3, 4, 5]))  # Output: [2, 4]

#####################################################################################
#####################################################################################
#-------------------------------------------------------------------------------
#  Exercise 18: Count different types in keyword arguments
#-------------------------------------------------------------------------------
def type_count(**kwargs):
    counts = {}
    for value in kwargs.values():
        t = type(value).__name__
        counts[t] = counts.get(t, 0) + 1
    return counts

# Example usage
print(type_count(a=1, b='string', c=1.0, d=True, e=False))
# Output: {'int': 1, 'str': 1, 'float': 1, 'bool': 2}

##################################################################################
##################################################################################
#-----------------------------------------------------------------------
#  Exercise 19: Mimic .split() method
#-----------------------------------------------------------------------
def my_split(text, sep=None):
    result = []
    word = ""
    for char in text:
        if sep is None:
            if char.isspace():
                if word:
                    result.append(word)
                    word = ""
            else:
                word += char
        else:
            if char == sep:
                result.append(word)
                word = ""
            else:
                word += char
    if word:
        result.append(word)
    return result

# Example usage
print(my_split("Hello world this is ChatGPT"))           # Default split by space
print(my_split("apple,banana,cherry", sep=","))         # Split by comma

#####################################################################################
#####################################################################################
#-----------------------------------------------------------------------
#  Exercise 20: Convert a string into password format
#-----------------------------------------------------------------------
def to_password(text):
    return '*' * len(text)

# Example usage
print(to_password("mypassword"))  # Output: "**********"
