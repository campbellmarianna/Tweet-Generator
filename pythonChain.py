# Notes from Poetry in Python: Using Markov Chains to Generate Texts by Omer Nevo
# Source: https://www.youtube.com/watch?v=-51qWZdA8zM
# Stopped at  13:30/3
# training - count of many times a word appears
# keep track of probability
#look at how many words appear after the words before it
# Keep track of 2 words before that starts the nth order of markov Chain
# Let's Code
# Simple __inti__
    # Pretty much

def __init__(self, order)
    self.order = order # order = how far back we remember
    self.group_size = self.order+1
    self.text = None # train text
    self.graph = {} # dict key= pairs of words, value: list of words we have seen come after that it

def train(self, filename):
    self.text = file(filename).read().split() # get text from file
    self.text = self.text + self.text[:self.order]
    # Order 2 key words that came before it and the value is the next word
    # go through one by one
    for i in range(0, len(self.text) - self.group_size):
        key = tuple(self.text[i:i+self.order])
        value = self.text[i+self.order]
        if key in self.graph: # Save it
            self.graph[key].append(value)
        else:
            self.graph[key] = value
# take random place in the text and start there
def generate(self, length):
    index = random.randint(0,len(self.text) - self.order)
    result
