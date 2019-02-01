"""
A histogram() function which takes a source_text argument and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
"""
source_text = "one fish two fish red fish blue fish"

def histogram(source_text):
    # Create words_list = ['one', 'fish', etc]
    words_list = source_text.split(" ")
    # print(words_list)
    # Create nested list
    nested_list = list()
    hist_counter = len(words_list)
    #print(hist_counter) # output 8
        # check if the first word is not in the list append it to the list
        # loop through words list
        for i in range(0, len(words_list)):
            # print(i) # output 0
            word = words_list[i]
            if word not in nested_list:
                counter_occ = 0
                nested_list.append([word, counter_occ])
                hist_counter -= 1
            # loop through list of list list
            # for j in range(0, len(nested_list)):
                # get actual word = i of word_list
                # word = words_list[i]
                # print(word) # one
                # create var count_occ
                # counter_occ = 0
                # check if word is not in list of list (bracket notation)
                # if word not in nested_list:
                    # increment counter
                    # counter_occ += 1
                    # append (word, counter) to list of list
                    # nested_list.append([word, counter_occ])
                # if word is in list
            else:
                print("HERE")
                # add 1 to current lisit of list list element nested
                counter_occ += 1
                nested_list[j]= [word, counter_occ]
                hist_counter -= 1
        print(nested_list)
        # return list of list

histogram(source_text)
