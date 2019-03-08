from dictogram import Dictogram # Inspired by Alexander Dejeu
from pprint import pprint
import random
import re
from sample import *

text = "one fish two blue fish fish red fish blue red fish END"
# text = 'how much wood would a wood chuck chuck if a wood chuck could chuck wood END'
texts_list = text.split()

def make_markov_model(words_list):
    """Generates histogram"""
    markov_model = dict() # create a dictionary

    for i in range (0, len(words_list)-2): # loop through the words
        word = words_list[i]
        # pprint(f"First word: {word}")
        word_2 = words_list[i+1]
        # pprint(f"Second word: {word_2}")
        current_words = (word, word_2)
        next_word = words_list[i+1+1]
        if current_words in markov_model:
            # We have to just append to the existing histogram
            markov_model[current_words].add_count(next_word)
        else:
            markov_model[current_words] = Dictogram([next_word])
    return markov_model

def generate_random_end(model):
    # To just generate any starting word uncomment line:
    # return random.choice(model.keys())

    # To generate a "valid" starting word use:
    # Valid starting words are words that started a sentence in the corpus
    print('MODEL: {}'.format(model))
    for k, v in model.items():
        # pprint(f"Key: {k}")
        for inner_key, inner_value in v.items():
            if inner_key == 'END':
                seed_word = 'END'
                while seed_word == 'END':
                    seed_word = non_uniform_sample(v)
                return (k[1],seed_word)

def generate_random_sentence(length, markov_model, words_list):
    current_words = generate_random_end(markov_model)
    sentence = [current_words[0], current_words[1]]
    for i in range(0, length):
        current_dictogram = markov_model[current_words]
        random_weighted_word = non_uniform_sample(current_dictogram)
        if random_weighted_word == 'END':
            break
        current_words = (current_words[1], random_weighted_word)
        sentence.append(current_words[1])
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'


model = make_markov_model(texts_list)
# pprint(model)
pprint(generate_random_sentence(4, model, texts_list))
