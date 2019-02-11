import random

def load_words():
    # with open('words.txt', 'r') as f:
    with open('new-words.txt', 'r') as f:
        # get each string separated by a space
        # put each string in an array
        f_contents = f.readlines() # list of each line of the file
        # Not from file:
        # f_contents = ["zythem", "Zythia", "zythum", "Zyzomys", "Zyzzogeton"]
    return f_contents


def get_rand_int_of_words(f_contents):
    words_list = []
    # f_contents = load_words()
    # print(f'Words in the file: {f_contents}') # Check output
    # pick a number by random that will be the number of words you want to get from the words file
    numOfWords = random.randrange(2, len(f_contents))
    # print(f"Random number of words: {numOfWords}") # Check output
    for wordIndex in range(0, numOfWords):
        word = f_contents[wordIndex]
        # print(f'The word: {word}') # Check output
        words_list.append(word)
    return words_list
        # f_word = f.readline()


def put_in_sentence(get__words_list):
    # clean_list = []
    sentence = ''
    words_list = get_words_list
    # print(f'Words based on random number: {words_list}') # Check output
    # use a for loop for every string in the array
    for word_index in range(0, len(words_list)):
        word = words_list[word_index]
        clean_word = word.rstrip('\n') # call on string to take out on the left or right on the string
        # clean_list.append(clean_word)
        # concatenate element to string
        sentence += " " + clean_word
        # what if you could use a join
    # return string
    return sentence

# print(put_in_sentence())
# clean_list()

if __name__ == '__main__':
    load_words = load_words()
    # print(f"Words from file: {load_words}")
    get_words_list = get_rand_int_of_words(load_words)
    # print(f"Random amount of words: {get_words_list}")
    put_in_sentence = put_in_sentence(get_words_list)
    # print(put_in_sentence)
