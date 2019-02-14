# module for cleaning up source text
def sanitize(f_contents):
    """
    A function that sanitizes words and returns a list.
    """
    clean_words = [] # create clean_words list
    for word in f_contents: # loop through list
        clean_word = word.rstrip('\n') # conduct r strip on each element
        clean_words.append(clean_word) # append word to to clean_words list
    return clean_words # return list
