import nltk
import re

# Define a list of keywords and their associated libraries
keyword_map = {
    "web scraping": "beautifulsoup4",
    "machine learning": "scikit-learn",
    "data visualization": "matplotlib",
    # Add more keywords and libraries as needed
}

# Tokenize and tag the input text using NLTK
text = input("Please enter your project keywords: ")
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

# Extract the relevant keywords using regular expressions
keywords = [word for (word, tag) in tags if re.match(r'^(NN|VBG)', tag)]

# Identify the associated libraries for each keyword
libraries = [keyword_map[keyword] for keyword in keywords if keyword in keyword_map]

# Display the results
if libraries:
    print("To implement your project, you will need to use the following libraries:")
    for library in libraries:
        print(library)
else:
    print("Sorry, we could not identify any relevant keywords.")
