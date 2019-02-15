#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        # self = []
        # word = 'how'
        # word_index = 2
        # print(f"Word Index: {word_index}")
        # word = [word, freq]
        found = False # Inspired by Jackson Ho
        for word_count in self: # loop through self
            if word_count[0] == word: # check if element string is equal to word (passed in)
                # word is in list - you have seen this word before
                temp_count = word_count[1] + count # create temporary count equal to element freq plus count
                self.remove(word_count)# remove element
                self.append((word, temp_count))# append new element with word and temp count
                self.tokens += count
                found = True # set found to True
                break
        if not found: # if not found
            # word is not in dictionary - you have not seen this word before
            self.append((word, count))# append word and count in a tuple
            self.types += 1 # increment types by 1
            self.tokens += count # increment tokens by count
    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        for word_count in self: # loop through self
            if word_count[0] == word: # if element is eqaul to self
                return word_count[1] # return the frequency of that element

        return 0 # return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        for word_count in self: # loop through self
            if word_count[0] == word: # check if element word is eqaul to self
                return True # return True

        return False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        for index in self: # loop through self
            if index == target: # check if element is equal to target
                return index # return index
            else: # otherwise
                return 'None' # return None

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
