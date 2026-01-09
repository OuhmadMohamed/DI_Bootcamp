###  Daily challenge Gold: Solve the Matrix
## Goal: Decrypt a hidden message from a matrix string by processing it column-wise and filtering characters.

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%
'''

# -----------------------------
# STEP 1: Convert string to 2D list
# -----------------------------

# Split the string into lines, remove empty lines
rows = [list(line) for line in MATRIX_STR.split("\n") if line.strip()]

matrix = rows

# Determine number of rows and columns
num_rows = len(matrix)
num_cols = len(matrix[0])

# -----------------------------
# STEP 2 + 3: Read column-wise & collect characters
# -----------------------------

raw_message = ""

for col in range(num_cols):
    for row in range(num_rows):
        char = matrix[row][col]
        raw_message += char

# -----------------------------
# STEP 4: Filter → keep letters, replace symbol-blocks with 1 space
# -----------------------------

decoded = ""
space_needed = False

for ch in raw_message:
    if ch.isalpha():
        # If we previously saw symbols, add one space
        if space_needed:
            decoded += " "
            space_needed = False
        decoded += ch
    else:
        # Symbol: mark that we need a space *if we later see a letter*
        space_needed = True

# -----------------------------
# STEP 5: Final output
# -----------------------------
print(decoded)
