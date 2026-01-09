#----------Exercise 1 : Upcoming Holiday----------------

import datetime

def upcoming_holiday():
    # Display today's date
    today = datetime.date.today()
    print(f"Today's date: {today}")

    current_year = today.year

    # List of major holidays with (month, day, name)
    holidays = [(1, 1, "New Year's Day"),]
        # Add more if needed, e.g., (1, 20, "Martin Luther King Jr. Day") etc.


    next_holiday = None
    min_days = float('inf')

    for month, day, name in holidays:
        try:
            holiday_date = datetime.date(current_year, month, day)
        except ValueError:
            # Handles invalid dates like Feb 30 (none here)
            continue

        if holiday_date < today:
            # Holiday already passed this year, check next year
            try:
                holiday_date = datetime.date(current_year + 1, month, day)
            except ValueError:
                continue

        days_left = (holiday_date - today).days

        if days_left < min_days and days_left >= 0:
            min_days = days_left
            next_holiday = (holiday_date, name)

    if next_holiday:
        holiday_date, name = next_holiday
        if min_days == 1:
            print(f"The next holiday is {name} tomorrow ({min_days} day).")
        elif min_days == 0:
            print(f"Today is {name}!")
        else:
            print(f"The next holiday is {name} in {min_days} days.")
        print(f"Holiday date: {holiday_date}")
    else:
        print("No upcoming holidays found in the list.")


############################################################################
##########################################################################3##

#----------Exercise 2 : How Old Are You On Jupiter?----------------

def how_old_are_you_on_planets(age_in_seconds: int) -> None:
    """
    Calculates and prints the age in years on each planet given an age in seconds.

    Parameters:
        age_in_seconds (int): Age in seconds (must be non-negative)
    """
    if age_in_seconds < 0:
        print("Age cannot be negative.")
        return

    # Earth year in seconds
    EARTH_YEAR_SECONDS = 31557600  # 365.25 days * 24 * 3600

    # Calculate age in Earth years
    earth_years = age_in_seconds / EARTH_YEAR_SECONDS

    # Orbital periods relative to Earth
    planets = {
        "Earth":   1.0,
        "Mercury": 0.2408467,
        "Venus":   0.61519726,
        "Mars":    1.8808158,
        "Jupiter": 11.862615,
        "Saturn":  29.447498,
        "Uranus":  84.016846,
        "Neptune": 164.79132
    }

    print(f"You are {age_in_seconds:,} seconds old.")
    print("Your age on different planets:")

    for planet, orbital_period in planets.items():
        age_on_planet = earth_years / orbital_period
        print(f"{planet:8}: {age_on_planet:.2f} years")


# Example usage
if __name__ == "__main__":
    # Test with the example given
    how_old_are_you_on_planets(1_000_000_000)

    # Another test
    print("\n" + "-"*40 + "\n")
    how_old_are_you_on_planets(1_234_567_890)
# Call the function
upcoming_holiday()

#############################################################################3
##############################################################################

#----------Exercise 3 : Regular Expression #1----------------

import re

def return_numbers(text: str) -> str:
    """
    Extracts all digits from the given string and returns them concatenated as a single string.

    Example:
        return_numbers('k5k3q2g5z6x9bn') -> '532569'

    Args:
        text (str): The input string that may contain numbers and other characters.

    Returns:
        str: A string containing only the digits found in the input, in the order they appear.
                 Returns an empty string if no digits are found.
    """
    # Find all digits in the string
    digits = re.findall(r'\d', text)

    # Join them into a single string
    return ''.join(digits)


# Test the function
if __name__ == "__main__":
    print(return_numbers('k5k3q2g5z6x9bn'))  # Output: 532569

    # Additional tests
    print(return_numbers('hello123world456'))     # Output: 123456
    print(return_numbers('noNumbersHere'))         # Output: (empty string)
    print(return_numbers('year2025python3.11'))   # Output: 2025311


####################################################################################
#####################################################################################
#----------Exercise 4 : Regular Expression #2----------------

import re

def check_full_name():
    while True:
        name = input("Enter your full name (e.g., John Doe): ").strip()

        # Regex explanation:
        # ^                 Start of string
        # [A-Z][a-z]+       First name: uppercase + one or more lowercase
        # \s                Single space
        # [A-Z][a-z]+       Last name: same pattern
        # $                 End of string
        pattern = r'^[A-Z][a-z]+\s[A-Z][a-z]+$'

        if re.match(pattern, name):
            print(f"Hello, {name}! Your name is valid.")
            break
        else:
            print("Invalid name. Please ensure:")
            print(" • Only letters and exactly one space")
            print(" • Two names only (first and last)")
            print(" • Each name starts with a capital letter")
            print("Try again.\n")

# Run it
check_full_name()

##################################################################################
#####################################################################################

#----------Exercise 5: Python Password Generator-----------

import random
import string
import re

def is_valid_password(password: str) -> bool:
    """
    Checks if the password meets all the required criteria:
    - At least 1 digit
    - At least 1 lowercase letter
    - At least 1 uppercase letter
    - At least 1 special character
    """
    if not re.search(r"\d", password):              # digit
        return False
    if not re.search(r"[a-z]", password):           # lowercase
        return False
    if not re.search(r"[A-Z]", password):           # uppercase
        return False
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};:'\"\\|,.<>/?~`]", password):  # special char
        return False
    return True


def generate_password(length: int) -> str:
    """
    Generates a secure password of the given length that is guaranteed to contain:
    - at least one digit
    - at least one lowercase
    - at least one uppercase
    - at least one special character
    The rest are random choices from all categories.
    """
    if length < 6:
        raise ValueError("Password length must be at least 6")

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{};:'\"\\|,.<>/?~`"

    # Ensure at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest with random choices from all pools
    all_chars = lowercase + uppercase + digits + special
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)


def test_password_generator():
    """
    Runs 100 tests with random lengths between 6 and 30.
    Verifies that every generated password:
    - Has the correct length
    - Meets all complexity requirements
    """
    print("Running 100 tests on password generator...\n")
    for i in range(1, 101):
        length = random.randint(6, 30)
        pwd = generate_password(length)

        # Check length
        if len(pwd) != length:
            print(f"Test {i} FAILED: Wrong length (expected {length}, got {len(pwd)})")
            return

        # Check validity
        if not is_valid_password(pwd):
            print(f"Test {i} FAILED: Password does not meet requirements: {pwd}")
            return

    print("All 100 tests PASSED! Password generator is working correctly.")


def main():
    """
    Main program: asks user for password length and generates a secure password.
    """
    print("Welcome to the Secure Password Generator!\n")

    while True:
        try:
            user_input = input("Enter desired password length (6 to 30 characters): ").strip()
            length = int(user_input)

            if 6 <= length <= 30:
                break
            else:
                print("Please enter a number between 6 and 30.\n")
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

    # Generate password
    password = generate_password(length)

    # Display result
    print("\n" + "="*50)
    print(f"Your new secure password ({length} characters):")
    print(f"\n{password}\n")
    print("IMPORTANT: Store this password in a safe place,")
    print("such as a trusted password manager.")
    print("="*50)


if __name__ == "__main__":
    # First run the automated tests
    test_password_generator()

    print("\n" + "-"*60 + "\n")

    # Then run the interactive program
    main()
