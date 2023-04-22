# 1: Print each word on a separate line, but in all uppercase
words = ['hello', 'hey', 'goodbye', 'yo', 'yes']
for word in words:
    print(word.upper())

# 2: Turn it into a function print_upper_words
def print_upper_words(words):
    """ Print all words in uppercase """
    for word in words:
        print(word.upper())

# 3: Change function so only prins words starting with 'e', either upper or lowecase
def print_upper_words_e(words):
    """ Print words in uppercase if they start with letter 'e' """
    for word in words:
        if word[0] == 'e' or word[0] == 'E':
            print(word.upper())

# print_upper_words_e(['hello','everyone'])

# 4: Make function more general. Accept set of letters
def print_upper_words_gen(words, must_start_with):
    """Print each word in the input list in all uppercase, but only if it starts with one of the letters in the input set."""
    for word in words: 
        if word[0] in must_start_with:
            print(word.upper())

# print_upper_words_gen(["hello","goodbye","no"],['h','g'])