from datetime import datetime

# 1. Ask for birthdate
birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

# 2. Convert to date
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
today = datetime.today()

# 3. Calculate age
age = today.year - birthdate.year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

# Last digit of the age
candles = age % 10

# 4. Build candles string
candles_str = "i" * candles if candles > 0 else ""

# 5. Display cake
print("       ___" + candles_str + "___")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~")

#Bonus : If they were born on a leap year, display two cakes !
if birthdate.year % 4 == 0 and (birthdate.year % 100 != 0 or birthdate.year % 400 == 0):
    print("\nSince you were born in a leap year, here's another cake for you!")
    print("       ___" + candles_str + "___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")
    
