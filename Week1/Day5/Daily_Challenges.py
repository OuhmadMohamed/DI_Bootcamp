###############  Daily challenge: Challenges  ####################

#------------Challenge 1: Sorting------------------

# Step 1: Get input from the user
words = input("Enter words separated by commas: ")

# Step 2: Split the string into a list
word_list = words.split(",")

# Step 3: Sort the list alphabetically
word_list.sort()

# Step 4: Join the sorted list into a string
sorted_words = ",".join(word_list)

# Step 5: Print the result
print(sorted_words)


########################################################
#######################################################

#------------Challenge 2: Longest Word------------------

def longest_word(sentence):
    # Step 2: Split the sentence into words
    words = sentence.split()

    # Step 3: Initialize variables
    longest = ""

    # Step 4 & 5: Iterate through the words and compare lengths
    for word in words:
        if len(word) > len(longest):
            longest = word

    # Step 6: Return the longest word
    return longest

print(longest_word("Margaret's toy is a pretty doll."))
# Output: Margaret's

print(longest_word("A thing of beauty is a joy forever."))
# Output: forever.

print(longest_word("Forgetfulness is by all means powerless!"))
# Output: Forgetfulness
