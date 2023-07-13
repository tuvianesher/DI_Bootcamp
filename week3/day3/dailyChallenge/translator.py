#pip install googletrans==4.0.0-rc1
from googletrans import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translator = Translator()

translations = {}
for word in french_words:
    translation = translator.translate(word, dest='en').text
    translations[word] = translation

print(translations)
