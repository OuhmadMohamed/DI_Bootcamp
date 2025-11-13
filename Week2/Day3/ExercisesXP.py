#   Exercise 1: Currencies
# Goal: Implement dunder methods for a Currency class to handle string representation, integer conversion, addition, and in-place addition.
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, (int, float)):
            return self.amount + other
        else:
            raise TypeError(f"Unsupported type for addition: {type(other)}")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, (int, float)):
            self.amount += other
        else:
            raise TypeError(f"Unsupported type for in-place addition: {type(other)}")
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('euro', 1)
c4 = Currency('euro', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

#print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>


##############################################################################""
#################################################################################"
#  Exercise 3: String module

import random 
import string
letters = string.ascii_letters
random_string = ''.join(random.choice(letters) for letter in range(5))

print(random_string)

#################################################################
# Exercise 4: Current Date
import datetime

def display_current_date():
    # Step 2: Get the current date
    current_date = datetime.date.today()
    
    # Step 3: Display the date
    print("Today's date is:", current_date)

# Call the function
display_current_date()

#############################################################################
#  Exercise 5: Amount of time left until January 1st
import datetime

def time_until_new_year():
    # Step 2: Get the current date and time
    now = datetime.datetime.now()

    # Step 3: Create a datetime object for January 1st of the next year
    next_year = now.year + 1
    new_year = datetime.datetime(year=next_year, month=1, day=1)

    # Step 4: Calculate the time difference
    time_left = new_year - now

    # Step 5: Display the time difference
    print(f"Time left until January 1st: {time_left}")

# Call the function
time_until_new_year()


##########################################################
# Exercise 6: Birthday and minutes
import datetime

def minutes_lived(birthdate_str):
    """
    Calculates how many minutes a person has lived based on their birthdate.
    The birthdate should be in the format 'YYYY-MM-DD'.
    """
    # Step 1: Convert the input string into a datetime object
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")

    # Step 2: Get the current date and time
    now = datetime.datetime.now()

    # Step 3: Calculate the difference
    time_lived = now - birthdate

    # Step 4: Convert the difference into minutes
    minutes = int(time_lived.total_seconds() / 60)

    # Step 5: Display the result
    print(f"You have lived approximately {minutes:,} minutes.")

# Example usage
minutes_lived("1999-06-24")

#######################################################################
# Exercise 7: Faker Module

# Step 1: Install the faker module (run this in your terminal or notebook)
# pip install faker

# Step 2: Import the faker module
from faker import Faker

# Step 3: Create an empty list of users
users = []

# Step 4: Create a function to add users
def generate_users(n):
    fake = Faker()  # Create a Faker instance
    for _ in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)

# Step 5: Call the function and print the users list
generate_users(5)

# Display the generated fake users
for user in users:
    print(f"name = {user['name']}\naddress = {user['address']}\nlanguage_code = {user['language_code']}")
    print("*******" * 3)

