Reverseinp = input()

# Split the sentence into words
words = Reverseinp.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join them back into a sentence
reversed_sentence = " ".join(reversed_words)

print(reversed_sentence)
