"""
A histogram() function which takes a source_text argument and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
"""
source_text = "one fish two fish red fish blue fish"

def histogram(source_text):
    histogram = dict()
    words_list = source_text.split(" ")
    for word in words_list:
        # print(f"A word from source text: {word}")
        if word not in histogram:
            # append word to histogram
            histogram[word] = 0
        # if word is in histogram increment value by 1
        histogram[word] += 1
    return histogram

"""
A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram.
"""

def unique_words(histogram):
    # print(histogram)
    counter = 0
    # loop through keys
    for k, v in histogram.items():
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

# def frequency():

print(unique_words(histogram(source_text)))
