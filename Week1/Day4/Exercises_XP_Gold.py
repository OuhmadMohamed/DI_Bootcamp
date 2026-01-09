#####################  Exercises XP Gold  ########################"
####################################################################"

##  Exercise 1 : When will I retire ?
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Let’s say retirement age is 67 for men, and 62 for women (born after April, 1947).
# 
# Hard-coded current date
CURRENT_YEAR = 2025
CURRENT_MONTH = 12
CURRENT_DAY = 7


# --------------------------------------------------
# 1. get_age(year, month, day)
# --------------------------------------------------
def get_age(year, month, day):
    age = CURRENT_YEAR - year

    # Adjust age if birthday hasn't happened yet this year
    if (month, day) > (CURRENT_MONTH, CURRENT_DAY):
        age -= 1

    return age


# --------------------------------------------------
# 2. can_retire(gender, date_of_birth)
# --------------------------------------------------
def can_retire(gender, date_of_birth):
    # Split date: "yyyy/mm/dd"
    year, month, day = map(int, date_of_birth.split("/"))

    age = get_age(year, month, day)

    # Retirement rules:
    # Men retire at 67
    # Women retire at 62 (born after April 1947 – safe to ignore since nobody today is older than that)
    if gender.lower() == "m":
        return age >= 67
    elif gender.lower() == "f":
        return age >= 62
    else:
        return False   # just in case invalid gender


# --------------------------------------------------
# Main program
# --------------------------------------------------

gender = input("Enter your gender (m/f): ")
dob = input("Enter your date of birth (YYYY/MM/DD): ")


####################################################################""
####################################################################""
# Exercise 2 : Sum
def compute_sum(X):
    X = str(X)
    return int(X) + int(X*2) + int(X*3) + int(X*4)

# Ask user for input
num = int(input("Enter a number: "))

# Compute and print result
result = compute_sum(num)
print(result)

if can_retire(gender, dob):
    print("You can retire!")
else:
    print("You cannot retire yet.")

###########################################################################"
###########################################################################"
##  Exercise 3 : Double Dice
import random

# -----------------------------------------------------
# 1. Function to simulate rolling one dice
# -----------------------------------------------------
def throw_dice():
    return random.randint(1, 6)

# -----------------------------------------------------
# 2. Function that throws two dice until doubles appear
# -----------------------------------------------------
def throw_until_doubles():
    count = 0
    while True:
        d1 = throw_dice()
        d2 = throw_dice()
        count += 1
        
        if d1 == d2:   # doubles reached
            return count

# -----------------------------------------------------
# 3. Main function
# -----------------------------------------------------
def main():
    results = []   # to store the number of throws for each double

    for _ in range(100):
        throws = throw_until_doubles()
        results.append(throws)

    total_throws = sum(results)
    average_throws = total_throws / len(results)

    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

# -----------------------------------------------------
# Run the program
# -----------------------------------------------------
main()
