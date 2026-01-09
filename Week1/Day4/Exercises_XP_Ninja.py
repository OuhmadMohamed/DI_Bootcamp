########## Exercise 1 : What’s your name ? ###############

def get_full_name(first_name, last_name, middle_name=""):
    """
    Returns the full name in title case.
    middle_name is optional.
    """
    if middle_name:  # if middle_name is not empty
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()


first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
middle = input("Please enter your middle name: ")

# If middle is empty string, the function will handle it
full_name = get_full_name(first, middle, last)

print("Your full name is:", full_name)





####################################################################
####################################################################

### Exercise 2 : From English to Morse #######
# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',  'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---','3': '...--',
    '4': '....-', '5': '.....', '6': '-....','7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/'  # space between words
}

# Reverse dictionary for Morse → English
MORSE_TO_ENGLISH = {v: k for k, v in MORSE_CODE_DICT.items()}

# --------------------------------------------------
# 1. Function to convert English text to Morse
# --------------------------------------------------
def english_to_morse(text):
    text = text.upper()
    morse = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
        else:
            morse.append('?')  # unknown character
    return ' '.join(morse)

# --------------------------------------------------
# 2. Function to convert Morse to English
# --------------------------------------------------
def morse_to_english(morse_code):
    words = morse_code.split(' / ')  # split words
    decoded_words = []
    for word in words:
        letters = word.split()  # split letters
        decoded_word = ''.join(MORSE_TO_ENGLISH.get(letter, '?') for letter in letters)
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)

# --------------------------------------------------
# Example usage
# --------------------------------------------------
text = input("Enter English text: ")
morse = english_to_morse(text)
print("Morse code:", morse)

# Example reverse translation
decoded = morse_to_english(morse)
print("Decoded back:", decoded)

#############################################################################
###############################################################################

########## Exercise 3 : Box of stars #######

def box_printer(*args):
    # Find the length of the longest string
    max_length = max(len(word) for word in args)
    
    # Print the top border
    print('*' * (max_length + 4))
    
    # Print each word with padding and side borders
    for word in args:
        print(f"* {word.ljust(max_length)} *")
    
    # Print the bottom border
    print('*' * (max_length + 4))


# -------------------------
# Example usage
# -------------------------
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")
