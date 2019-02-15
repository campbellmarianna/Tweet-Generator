# module for generating histograms from a list of tokens
# old histograms into this file
# any functions that help you convert list to histogram

# histogram_dict
def dictogram(source_text):
    """
    A histogram() function which takes a source_text argument and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
    """
    histogram = dict() #Issue: histogram scoped to this function - might need to be global
    words_list = source_text.split(" ")
    # print(words_list)
    for word in words_list:
        # print(f"A word from source text: {word}")
        if word not in histogram:
            # append word to histogram
            histogram[word] = 0
        # if word is in histogram increment value by 1
        histogram[word] += 1
    return histogram

# histogram_list
source_text = "one fish two fish red fish blue fish"

def listogram(source_text):
    """
    A histogram() function which takes a source_text argument and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
    """
    # Create words_list
    words_list = source_text.split(" ")
    # print(words_list)
    # Create nested list
    nested_list = []
    # print(nested_list)
    # loop through words list
    for word in words_list:
        # print(word)
        found = False
        if len(nested_list) == 0:
            nested_list.append([word, 1])
        else:
            # loop through nested list
            for nested_word in nested_list:
                # check if word is the same as nested word[0]
                if word in nested_word[0]:
                    found = True
                    # increment the counter for duplicates
                    nested_word[1] += 1
                    # print(nested_list)
                    break
            # check if found is false
            if not found:
                # append nested_list([word, 1])
                nested_list.append([word, 1])
    return nested_list

list =(listogram(source_text))
print(list)


#histogram_tuple
def tupogram(source_text): # Inspired by Jackson Ho
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


def unique_words(histogram):
    """
    A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram.
    """
    # print(histogram)
    counter = 0
    # loop through keys
    for k, v in histogram.items(): #What is going on with k + v (non-conventional)
        # print(f"The key is: {k}")
        # check if key's value is equal to one
        if histogram[k] is 1:
            # print(f"The value should be 1. It is {histogram[k]}")
            # increment counter by 1
            counter +=1
            # print(f"Counter: {counter}")
        # if words is in unique list print duplicate
        # else:
            # print(f"The value should be more than 1. It is {histogram[k]}")
            # print('Duplicate')
    return counter


def frequency(word, histogram):
    """
    A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
    """
    counter = 0
    # loop through dict
    for k,v in histogram.items(): #Use of k and v again
    # print(f"This should be a word. It is {k}")
    # print(f"{v}")
    #check if the word is the same as the source word and that the key's value is more than one
        if word == k and v > 1:
            # print(f"This should be a word that repeats in the source text. It is {k}")
            # increment counter by key's value
                counter += v
    return counter
