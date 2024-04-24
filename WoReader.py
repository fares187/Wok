import spacy
from collections import Counter

# Loads English language model
# python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")


# Reads the contents of the file
with open("random_paragraphs.txt", "r") as file:
    text = file.read()

nlp.max_length = len(text) + 100000

# Processes the text with spaCy
doc = nlp(text)

# Defines a list of stop words
stop_words = spacy.lang.en.stop_words.STOP_WORDS

# Removes stop words and punctuation, and count word frequencies
word_freq = Counter(token.text.lower() for token in doc if token.text.lower() not in stop_words and not token.is_punct)

# Displays word frequency count
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")
