import nltk
nltk.download("punkt")

from nltk.stem import PorterStemmer

nltk.download("punkt")  # Download the required data

# Create a Porter Stemmer instance
stemmer = PorterStemmer()

# Example sentences for stemming
sentences = [
    "Vijay missed the bus",
    "The train is late today because of rain",
    "We use chatgpt to get answers for the questions"
]

# Tokenize each sentence and apply stemming
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    stemmed_words = [stemmer.stem(word) for word in words]
    stemmed_sentence = " ".join(stemmed_words)
    print(f"Original: {sentence}")
    print(f"Stemmed: {stemmed_sentence}\n")
