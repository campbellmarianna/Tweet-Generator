source_text = "one fish two fish red fish blue fish"

def histogram(source_text): # Inspired by Jackson Ho
    # create words_list
    words_list = source_text.split(' ')
    # create list_of_tuple
    list_of_tuples = []
    # append first [word, 1] to list_of_tuples
    list_of_tuples.append((words_list[0], 0))
    # loop through words_list
    for word in words_list:
        # create flag found = False
        found = False
        # loop through list of tuples
        for index, value in enumerate(list_of_tuples):
            # check if word is the same as tuple[0]
            if value[0] == word:
                #create var store freq + increment freq
                num = value[1] + 1
                # set flag to True
                found = True
                # take out that tuple
                list_of_tuples.pop(index)
                # append the word with the new freq
                list_of_tuples.append((word, num))
                # break
                break
        # if the word is not found
        if not found:
            # append the (word, 1) to the list of tuple
            list_of_tuples.append((word, 1))
    # return list of tuple
    return list_of_tuples

histogram(source_text)
