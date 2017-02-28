#/bin/python

from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        words = [line.strip() for line in f.readlines()]
    return words
    

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[letter.capitalize()] for letter in word if letter.capitalize() in LETTER_SCORES.keys()]) 
    

def max_word_value(*word_lists):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    words = []
    if not word_lists:
        words = load_words()
    else:
        words = sum(word_lists, ()) 
    scores = [(calc_word_value(word), word) for word in words]
    
    return max(scores)[1]

if __name__ == "__main__":
    pass # run unittests to validate
