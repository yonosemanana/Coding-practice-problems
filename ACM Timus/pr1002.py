from sys import stdin, stdout
import sys

sys.setrecursionlimit(10000)

codes = {'1': 'ij', '2': 'abc', '3': 'def', '4': 'gh', '5': 'kl', '6': 'mn', '7': 'prs', '8': 'tuv', '9': 'wxy', '0': 'oqz'}
reverse_codes = {'i': '1', 'j': '1',
                 'a': '2', 'b': '2', 'c': '2',
                 'd': '3', 'e': '3', 'f': '3',
                 'g': '4', 'h': '4',
                 'k': '5', 'l': '5',
                 'm': '6', 'n': '6',
                 'p': '7', 'r': '7', 's': '7',
                 't': '8', 'u': '8', 'v': '8',
                 'w': '9', 'x': '9', 'y': '9',
                 'o': '0', 'q': '0', 'z': '0'}

def word_to_num(word):
    """
    :param word:
    :return:
    """
    return str([reverse_codes[letter] for letter in word])


def search_words(index):
    """
    :param lines:
    :param index:
    :return:
    """
    telnum = lines[index]
    word_count = int(lines[index+1])
    words = lines[index+2:index+2+word_count]

    solution = []
    node = {'path': [],
            'checked': False}

    possible_paths = {('',): {'checked': False}}

    node = possible_paths.popitem()
    for word in words:
        possible_paths[(node[0], word,)] = {'checked': False}

    while possible_paths != set():
        pass

    return telnum, word_count, words

index = 0
lines = stdin.readlines()
while lines[index] != '-1':
    telnum, word_count, words = search_words(index)
    print(telnum, word_count, words)
    index = index + 2 + word_count