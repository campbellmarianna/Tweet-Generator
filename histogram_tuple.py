source_text = "one fish two fish red fish blue fish"

def histogram(source_text):
    # create words_list
    words_list = source_text.split(" ")
    # print(f"Words list: {words_list}")
    # create list_of_tuples = []
    list_of_tuples = []
    # print(list_of_tuples)
    # loop through words_list
    for word in words_list:
        # found = False
        found = False
        # check if list of tuples is = 0
        if len(list_of_tuples) == 0:
            # append first word to list of tuples
            list_of_tuples.append((word, 1))
            # print(list_of_tuples)
        # else
        else:
            # loop (index, tuple) through enumerate list of tuples
            for index, tuple in enumerate(list_of_tuples):
                # print(f"This should be a string: {tuple[0]}")
                # check if word is the same as tuple word
                if word == tuple[0]:
                    # create var to store tuple int
                    # increment var by 1
                    freq = tuple[1] + 1
                    # print(f"This should be a number {index}")
                    # pop tuple out of list
                    list_of_tuples.pop(index)
                    # print(f"List before: {list_of_tuples}")
                    # append tuple with word and new frequency
                    list_of_tuples.append((word, freq))
                    # print(f"List after: {list_of_tuples}")
                    # found is true
                    found = True
                    # break
                    break
                # check if not found
                if not found:
                    # append (word) to list of tuple
                    list_of_tuples.append((word, 1))
    return(list_of_tuples)

print(histogram(source_text))
