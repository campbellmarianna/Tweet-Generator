"""
A histogram() function which takes a source_text argument and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
"""
source_text = """As our consumeristic society bumps up against creational limits, technological and economic progress is
often pitted against environmental stewardship. Those opposed to governmental regulation of pollution
and resource use claim that these restrictions hinder the growth of the economy, while those in favor of
additional control, acknowledge that we will likely have to make sacrifices as a result. The adversarial
relationship between humankind and the rest of the creation has a long history with many ramifications.
This paper begins to explore how this twisted relationship has distorted the engineering design process by
narrowing the definition of the engineer’s stewardship task. By revisiting the garden and our original
mandate, our understanding of our stewardship task is broadened from one of “doing less harm”1
 to one
of “enabling creation to flourish”. A richer understanding of our proper relationship to the rest of creation
has the potential to spur creative solutions to meet the needs of our world while pointing to Christ’s
kingdom of shalom."""

def histogram(source_text):
    histogram = dict()
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

"""
A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
"""

def frequency(word, histogram):
    counter = 0
    # loop through dict
    for k,v in histogram.items():
        # print(f"This should be a word. It is {k}")
        # print(f"{v}")
        #check if the word is the same as the source word and that the key's value is more than one
        if word == k and v > 1:
            # print(f"This should be a word that repeats in the source text. It is {k}")
            # increment counter by key's value
            counter += v
    return counter

# print(histogram(source_text))
# print(unique_words(histogram(source_text)))
# print(frequency('creation', histogram(source_text)))
