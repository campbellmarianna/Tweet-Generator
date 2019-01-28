import random


def load_words():
    with open('words.txt', 'r') as f:
        # get each string separated by a space
        # put each string in an array
        f_contents = f.readlines()
        # Not from file:
        # f_contents = ["zythem", "Zythia", "zythum", "Zyzomys", "Zyzzogeton"]
    return f_contents

# print(load_words())
# list of the words from file

def get_rand_int_of_words():
    words_list = []
    f_contents = load_words()
    print(f'Words in the file: {f_contents}')
    # pick a number by random that will be the number of words you want to get from the words file
    numOfWords = random.randint(0, len(f_contents) -1)
    print(f"Random number of words: {numOfWords}")
    for wordIndex in range(0, numOfWords):
        word = f_contents[wordIndex]
        print(f'The word: {word}')
        new_word = word.replace('/n', '')
        print(f'This is the new word: {new_word}')
        words_list.append(new_word)
    return words_list
        # f_word = f.readline()


def put_in_sentence():
    sentence = ''
    words_list = get_rand_int_of_words()
    print(f'Words based on random number: {words_list}')
    # use a for loop for every string in the array
    for word in range(0, len(words_list)):
        word = str(words_list[word])
        sentence += word
        # concatenate element to string
    # print(f'The sentence: {sentence}')
    # return string
    return sentence

print(put_in_sentence())
