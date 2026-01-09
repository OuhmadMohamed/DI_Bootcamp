
import random
def random_word():
    word_list =  ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    chosen_word = random.choice(word_list)  
    print(chosen_word)
    display_word = ['*' for i in chosen_word]
    print(display_word)
    return display_word, chosen_word

def letter(chosen_word, display_word,attempts):
    letter = input("Guess a letter: ").lower()
    if letter in chosen_word and len(letter) == 1:
        for index, char in enumerate(chosen_word):
            if char == letter:
                display_word[index] = letter
        print("Good guess!")
        print(''.join(display_word))
    else:
        print(f"Sorry, the letter '{letter}' is not in the word.")
        print(''.join(display_word))
        attempts -= 1
    return attempts

def hangman():
    display_word, chosen_word = random_word()
    attempts = 6
    while '*' in display_word:
        letter(chosen_word, display_word, attempts)
        if '*' not in display_word:
            print("Congratulations! You've guessed the word correctly.")
            break
hangman()
