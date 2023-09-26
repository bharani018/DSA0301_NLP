import nltk
nltk.download('averaged_perceptron_tagger')


from nltk.tokenize import word_tokenize

# Sample text
text = "Natural language processing is a subfield of artificial intelligence."

# Tokenize the text into words
words = word_tokenize(text)

# Download the missing resource
nltk.download('averaged_perceptron_tagger')

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Print the POS tagged result
print(pos_tags)
