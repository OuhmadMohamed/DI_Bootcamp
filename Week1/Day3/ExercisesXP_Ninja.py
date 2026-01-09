# Given string
cars_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Convert to list (split by comma + remove spaces)
cars_list = [car.strip() for car in cars_string.split(",")]

# How many manufacturers?
print(f"There are {len(cars_list)} manufacturers in the list.")

# Print list in reverse alphabetical order (Z-A)
print("Manufacturers in reverse order (Z-A):")
print(sorted(cars_list, reverse=True))

# Count how many names contain 'o'
count_o = sum(1 for name in cars_list if 'o' in name.lower())

# Count how many names DO NOT contain 'i'
count_no_i = sum(1 for name in cars_list if 'i' not in name.lower())

print(f"Number of manufacturers with the letter 'o': {count_o}")
print(f"Number of manufacturers without the letter 'i': {count_no_i}")

# ---------------- BONUS PART ----------------

bonus_list = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

# Remove duplicates using set
unique_companies = sorted(set(bonus_list))

# Print companies as comma-separated string
print("\nCompanies without duplicates:")
print(", ".join(unique_companies))

# Count after removing duplicates
print(f"There are now {len(unique_companies)} unique companies.")

# Bonus 2: print manufacturers in A-Z but reverse letters of each name
reversed_names = [name[::-1] for name in unique_companies]

print("\nManufacturers A-Z but letters reversed:")
print(reversed_names)
