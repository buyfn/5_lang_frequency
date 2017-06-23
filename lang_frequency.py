import os
import sys
import string
import operator
import collections


def load_text(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text, count=10):
    punctuation = string.punctuation + '—«»…'
    stripped_text = ''.join([char.lower() for char in text
                             if char not in punctuation])
    words = stripped_text.split()
    word_count = collections.Counter(words)
    sorted_words = sorted(word_count.items(),
                          key=operator.itemgetter(1),
                          reverse=True)

    return sorted_words[:count]


def print_frequent_words(words_dict):
    for word in words_dict:
        print('{}: {}'.format(word[0], word[1]))


if __name__ == '__main__':
    current_directory = os.getcwd()
    try:
        path = os.path.join(current_directory, sys.argv[1])
    except IndexError:
        sys.exit('Need to specify text file to count words in')

    text = load_text(path)
    if text:
        frequent_words = get_most_frequent_words(text)
        print('\nMost frequent words in the file:')
        print_frequent_words(frequent_words)
    else:
        print('Wrong filepath')
