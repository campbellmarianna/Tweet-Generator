import random
from pprint import pprint

source_text = "one fish two fish red fish blue fish"

def histogram(source_text):
    histogram = dict() #Issue: histogram scoped to this function - might need to be global
    words_list = source_text.split(" ")
    for word in words_list:
        if word not in histogram:
            # append word to histogram
            histogram[word] = 0
        # if word is in histogram increment value by 1
        histogram[word] += 1
    return histogram

def sample(histogram): # create function with params histogram
    words_list = [] # create a words_list
    for inner_list in histogram: # loop through histogram
        word = inner_list[0]
        words_list.append(word) # append word to words_list
    word_index = random.randint(0, len(words_list) - 1) # for the length of the words_list get a random number in that range use that as an index in the words_list
    return words_list[word_index] # return the words_list element at that index

def automate_sample(histogram): # create function automate_test
    counter = 10000 # create counter equal to 10
    hist_list = list() # create a hist_list
    while counter > 0: # create a while loop with condition counter > 0
        word = non_uniform_sample(histogram)
        found = False
        if len(hist_list) == 0:
            hist_list.append([word, 1]) # append returning value to hist_list
        else: # do hist_logic
            for inner_list in hist_list: # loop through hist_list
                if word == inner_list[0]:
                    found = True
                    inner_list[1] += 1
                    break
            if not found:
                hist_list.append([word, 1])
        counter -= 1
    return hist_list # return histlist

def non_uniform_sample(histogram): # create non-uniform sample function
    """
    Generate a random word based on non-uniform distribution
    """
    words_frequency = 0 # create words_frequency
    for key, value in histogram.items(): # loop through histogram
        words_frequency += value # append word to words_frequency
    random_num = random.randint(0, words_frequency-1) # generate random number
    count = 0 # create count var
    for word, freq in histogram.items(): # loop through hist.items
        count += freq # increment count by frequency
        if random_num < count: # check if random_num is less than count
            return word # return word

hist = histogram(source_text)

pprint(automate_sample(hist))

# pprint(non_uniform_sample(hist))
