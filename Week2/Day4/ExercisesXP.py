# Exercise 1: Random Sentence Generator
import random
# Step 1: Create the get_words_from_file function
def get_words_from_file(file_path):
    """Reads words from a text file and returns them as a list."""
    try:
        with open(file_path) as file:
            word1 = file.read().split()
            return word1
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []


# Step 2: Create the get_random_sentence function
def get_random_sentence(length):
    """Generates a random sentence with a given number of words."""
    word = get_words_from_file("words.txt")  
    if not word:
        return "No words available to generate a sentence."

    random_words = [random.choice(word) for _ in range(length)]
    sentence = " ".join(random_words).lower()
    return sentence


# Step 3: Create the main function
def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program generates a random sentence from a list of words.\n")

    try:
        length = int(input("Enter the desired sentence length (between 2 and 20): "))
        if length < 2 or length > 20:
            print("Error: Please enter a number between 2 and 20.")
            return
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    sentence = get_random_sentence(length)
    print("\nYour random sentence is:\n")
    print(sentence)


# Run the program
if __name__ == "__main__":
    main()


