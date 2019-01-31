"""
A histogram() function which takes a source_text argument and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
"""
source_text = "one fish two fish red fish blue fish"

def histogram(source_text):
    # Create words_list = ['one', 'fish', etc]
    words_list = source_text.split(" ")
    # print(words_list)
    # Create list_of List list
    list_of_list = list()
    # loop through words list
    for i in range(0, len(words_list)):
        # print(i) # output 0
        # loop through list of list list
        for j in range(0, len(list_of_list)):
            # get actual word = i of word_list
            word = words_list[i]
            print(word) # one
            # create var count_occ
            counter_occ = 0
            # check if word is not in list of list (bracket notation)
            if word not in list_of_list:
                # increment counter
                counter_occ += 1
                # append (word, counter) to list of list
                list_of_list.append([word, counter_occ])
            # if word is in list
            else:
                # add 1 to current lisit of list list element list_of
                list_of_list[j][1] += 1
    print(list_of_list)
    # return list of list

histogram(source_text)
