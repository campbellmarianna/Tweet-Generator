# markOf function that walks through histogram
# your sentence function

def get_rand_int_of_words(f_contents):
    """
    A function that is given a list of sanitized words and returns a random list of words.
    """
    words_list = []
    # pick a number by random that will be the number of words you want to get from the words file
    numOfWords = random.randrange(2, len(f_contents))
    # print(f"Random number of words: {numOfWords}") # Check output
    for wordIndex in range(0, numOfWords):
        word = f_contents[wordIndex]
        # print(f'The word: {word}') # Check output
        words_list.append(word)
    return words_list
    
def put_in_sentence(get_words_list):
    # clean_list = []
    sentence = ''
    words_list = get_words_list
    # print(f'Words based on random number: {words_list}') # Check output
    # use a for loop for every string in the array
    for word_index in range(0, len(words_list)):
        word = words_list[word_index]
        # clean_word = word.rstrip('\n') # call on string to take out on the left or right on the string
        # clean_list.append(clean_word)
        # concatenate element to string
        sentence += " " + word
        # what if you could use a join
    # return string
    return sentence
