import nltk
import re

# Define a dictionary of keywords and their associated libraries
keyword_map = {
    "web scraping": "beautifulsoup4",
    "machine learning": "scikit-learn",
    "data visualization": "matplotlib",
    "data analysis": "pandas",
    "natural language processing": "nltk",
    # Add more keywords and libraries as needed
}

def get_libraries(keywords):
    # Identify the associated libraries for each keyword
    libraries = [keyword_map[keyword] for keyword in keywords if keyword in keyword_map]
    return libraries

def main():
    # Get user input and tokenize it using NLTK
    text = input("Please enter your project keywords: ")
    tokens = nltk.word_tokenize(text)
    
    # Tag the tokens with their part-of-speech using NLTK
    tags = nltk.pos_tag(tokens)
    
    # Extract the relevant keywords using regular expressions
    keywords = [word.lower() for (word, tag) in tags if re.match(r'^(NN|VBG)', tag)]
    
    # Get the associated libraries for the extracted keywords
    libraries = get_libraries(keywords)
    
    # Display the results
    if libraries:
        print("To implement your project, you will need to use the following libraries: ")
        for library in libraries:
            print(library)
    else:
        print("Sorry, we could not identify any relevant keywords.")
        
if __name__ == '__main__':
    main()
