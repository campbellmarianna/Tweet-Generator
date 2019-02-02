"""
A histogram() function which takes a source_text argument and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
"""
source_text = "one fish two fish red fish blue fish"

def histogram(source_text):
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
    print(nested_list)

histogram(source_text)
