# This python code will find similar looking words from pre-defined array
from difflib import get_close_matches

word_list = ["apple", "application", "appliance", "banana", "grape", "pineapple", "grapefruit", "orange"]

def find_similar_words(input_word, word_list, cutoff=0.6):
    similar_words = get_close_matches(input_word, word_list, n=5, cutoff=cutoff)
    return similar_words

user_word = input("Enter a word: ").strip().lower()

matches = find_similar_words(user_word, word_list)

if matches:
    print("Did you mean one of these?")
    print(", ".join(matches))
else:
    print("No similar words found.")
