import json
from difflib import get_close_matches

collection = json.load(open("collection.json"))

def lookup(word):
    word = word.lower()
    if word in collection:
        return collection[word]
    elif len(get_close_matches(word, collection.keys())) > 0:
        yn = input("Are you looking for the word %s ? Enter Y for Yes or N for No: " % get_close_matches(word, collection.keys())[0])
        if yn == "Y":
            return collection[get_close_matches(word, collection.keys())[0]]
        elif yn == "N":
            return "Word not found. Please try again."
        else:
            return "Please enter either Y or N"
    else:
        return "No word entered"

print('\n***** WELCOME TO THE PYTHON ENGLISH DICTIONARY *****\n')
word = input("Enter word: ")
output = lookup(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)