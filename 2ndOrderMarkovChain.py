from dictogram import Dictogram # Inspired by Alexander Dejeu
from pprint import pprint
import random
from sample import *

text = "one fish two blue fish fish red fish blue red fish END"
texts_list = text.split()

def make_higher_order_markov_model(order, data):
    """Creates a histogram"""
    markov_model = dict()

    for i in range(0, len(data)-order):
        window = tuple(data[i: i+order]) # Create the window
        print(f"Window: {window}")
        if window in markov_model:     # Add to the dictionary
            print(f"**********What is being added:{data[i+order]}")
            markov_model[window].add_count([data[i+order]]) # We have to just append to the existing Dictogram
        else:
            markov_model[window] = Dictogram([data[i+order]])
    return markov_model

def generate_random_start(model):
    print("IN FUNCTION")
    print('MODEL: {}'.format(model))
    for k, v in model.items():
        # pprint(f"Key: {k}")
        pprint(f"Value: {v}")
        for inner_key, inner_value in v.items():
            if inner_key == 'END':
                seed_word = 'END'
                while seed_word == 'END':
                    seed_word = non_uniform_sample(v)
                    # break #seed_word = 'FOUND'
                return (k[1],seed_word)

def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    print("I'm getting the current word")
    sentence = [current_word]
    for i in range(0, length):
        current_dictogram = markov_model[current_word]
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'
    return sentence

model = make_higher_order_markov_model(2, texts_list)
pprint(generate_random_start(model))
# pprint(generate_random_sentence(5, model))
