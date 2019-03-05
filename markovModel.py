from dictogram import Dictogram # Inspired by Alexander Dejeu
from pprint import pprint

# text = "one fish two fish red fish blue fish"
text = 'how much wood would a wood chuck chuck if a wood chuck could chuck wood'
texts_list = text.split()

def make_markov_model(words_list):
    """Generates sentences"""
    markov_model = dict() # create a dictionary
    print(markov_model)
    for i in range (0, len(words_list)-1): # loop through the words
        current_word = words_list[i]
        next_word = words_list[i+1]
        print(next_word)
        if current_word in markov_model:
            # We have to just append to the existing histogram
            markov_model[current_word].add_count(next_word)
        else:
            markov_model[current_word] = Dictogram([next_word])
    return markov_model

pprint(make_markov_model(texts_list))
