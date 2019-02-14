# module for creating lists of tokens from a text
# turns file into list

def load_words():
    """
    A function that returns a list of words from a file.
    """
    with open('new-words.txt', 'r') as f:
        f_contents = f.readlines() # list of each line of the file
        # f_contents = ["zythem", "Zythia", "zythum", "Zyzomys", "Zyzzogeton"]
        print(f_contents)
    return f_contents
