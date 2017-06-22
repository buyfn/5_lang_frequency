import os
import sys
import string
import operator


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def count_words(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def get_most_frequent_words(text, count=10):
    punctuation = string.punctuation + '—«»…'
    stripped_text = ''.join([char.lower() for char in file_content
                             if char not in punctuation])
    words = stripped_text.split()
    word_count = count_words(words)

    sorted_words = sorted(word_count.items(),
                          key=operator.itemgetter(1),
                          reverse=True)

    return sorted_words[:count]


if __name__ == '__main__':
    current_directory = os.getcwd()
    try:
        path = os.path.join(current_directory, sys.argv[1])
    except IndexError:
        sys.exit('Need to specify text file to count words in')

    file_content = load_data(path)
    if file_content:
        frequent_words = get_most_frequent_words(file_content)
        print('\nMost frequent words in the file:')
        for elt in frequent_words:
            print('{}: {}'.format(elt[0], elt[1]))
    else:
        print('Wrong filepath')
