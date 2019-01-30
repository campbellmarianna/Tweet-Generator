source_text = "one fish two fish red fish blue fish"

def histogram(source_text):
    histogram = dict()
    words_list = source_text.split(" ")
    # hist_copy = histogram.copy()
    for word in words_list:
        print(f"A word from source text: {word}")
        if word not in histogram:
            # append word to histogram
            histogram[word] = 0
        # if word is in histogram increment value by 1
        histogram[word] += 1
    return histogram
# def unique_words():

# def frequency():

print(histogram(source_text))
