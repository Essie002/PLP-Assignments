import json
from difflib import get_close_matches

def load_dictionary(data_file):
    with open(data_file, 'r') as f:
        data = json.load(f)
    return data

def get_definition(word, data):
    word = word.lower()  # Convert input to lowercase for case insensitivity
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        return f"Word not found. Did you mean '{close_match}'?"
    else:
        return "Word not found in dictionary."

# Load dictionary data
dictionary_data = load_dictionary('C:/Users/USER/Desktop/PLP-Assignments/Week4/Mini_project/data.json')
#Testing
word_input = input("Enter a word to get its definition: ")
definition = get_definition(word_input, dictionary_data)
print(definition)
