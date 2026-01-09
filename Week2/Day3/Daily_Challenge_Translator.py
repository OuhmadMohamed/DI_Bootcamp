#import sys
#!{sys.executable} -m pip install googletrans==4.0.0-rc1
from googletrans import Translator

# Initialize translator
translator = Translator()

# Input data
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# Translation dictionary
translations = {}

for word in french_words:
    translated = translator.translate(word, src='fr', dest='en')
    translations[word] = translated.text

# Display result
print(translations)
