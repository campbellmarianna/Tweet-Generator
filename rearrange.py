# This code randomly .
import random, sys
from datetime import datetime

start_time = datetime.now()
# Capture the input from the terminal
words = sys.argv[1:]

def rearrange_words():
    """
    A function that randomly rearranges a set of words provided as command-line arguments to the script 
    """
    # Run a loop that runs for how many elements in the list
    for w in range(0, len(words)):
        # pair random index with list
        rand_index = random.randint(0, len(words) -1)
        # word = words[w]
        # remove element from list
        word_taken_out = words.pop(rand_index)
        # add element to the end of the list
        words.append(word_taken_out)
        return ' '.join(words)

print(rearrange_words())
print(datetime.now() - start_time)
