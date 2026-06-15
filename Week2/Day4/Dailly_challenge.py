import string
import re


class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)

        if count == 0:
            return f"'{word}' not found in the text."
        return count

    def most_common_word(self):
        words = self.text.split()
        frequencies = {}

        for word in words:
            frequencies[word] = frequencies.get(word, 0) + 1

        return max(frequencies, key=frequencies.get)

    def unique_words(self):
        words = self.text.split()
        return list(set(words))

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return cls(content)


class TextModification(Text):

    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        return self.text.translate(translator)

    def remove_stop_words(self):
        stop_words = {
            "a", "an", "the", "is", "are", "was", "were", "am",
            "be", "been", "being", "and", "or", "but", "if",
            "then", "else", "for", "of", "on", "in", "at",
            "to", "from", "with", "by", "as", "that", "this",
            "these", "those", "it", "its", "he", "she", "they",
            "them", "his", "her", "their", "you", "your", "we",
            "our", "i", "my", "me"
        }

        words = self.text.split()

        filtered_words = [
            word for word in words
            if word.lower() not in stop_words
        ]

        return " ".join(filtered_words)

    def remove_special_characters(self):
        # Keeps only letters, numbers, and spaces
        return re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
