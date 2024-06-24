

import requests
from collections import Counter
import re

# Step 1: Import Libraries
# - requests: to download the corpus
# - Counter: to count word frequencies
# - re: for regular expression operations

# Step 2: Download the Corpus
url = "https://norvig.com/ngrams/shakespeare.txt"
response = requests.get(url)
corpus = response.text

# Step 3: Lowercase the Text
# Convert all characters in the corpus to lowercase to ensure uniformity
corpus = corpus.lower()

# Step 4: Tokenize the Text
# Use regular expressions to find all words in the corpus
# The pattern \b\w+\b matches sequences of word characters (letters, digits, and underscores) surrounded by word boundaries
words = re.findall(r'\b\w+\b', corpus)

# Step 5: Count Word Frequencies
# Create a Counter object to count the frequency of each word in the list of words
word_counts = Counter(words)

# Step 6: Get Most Common Words
# Retrieve the 10 most common words and their frequencies
most_common_words = word_counts.most_common(10)

# Step 7: Print the Results
# Print the most common words along with their counts
for word, count in most_common_words:
    print(f"{count} {word}")