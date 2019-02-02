source_text = "one fish two fish red fish blue fish"

def histogram(source_text):
    words_list = source_text.split(" ")
    # create a list_of_tuples
    list_of_tuples = []
    # loop words_list
    for word in words_list:
        # loop through list_of_tuple / for tuple in list_of_tuple
        found = False
        for index, tuple in list_of_tuple:
            #check if the first value in the current tuple is the word
            if word is tuple[0]:
                # set found to true
                # store value2
                freq = tuple[1] + 1
                list_of_tuples.delete(tuple)
                list_of_tuples.append((tuple[0], freq))
                break
                # if it is in there
                # make the index[1] the number a variable
                # remove that tuple
        if not found:
            list_of_tuples.append((word, 1))
    return list_of_tuple
