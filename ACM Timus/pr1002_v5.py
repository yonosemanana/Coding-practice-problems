### Site: https://acm.timus.ru/
### Problem: 1002

### Failed on Test 7

from sys import stdin, stdout

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
    res = ''
    for letter in word:
        res += reverse_codes[letter]
    return res


def search_words(telnum, words):
    """
    :param telnum:
    :param words:
    :return:
    """

    solution = []
    possible_paths = [{'': {'path': [], 'num_index': 0}}]

    num_index = 0
    while len(possible_paths) > 0:
        node = possible_paths.pop(0)
        node_str = node.popitem()
        node_num = word_to_num(node_str)

        # print(node, node_str, node_num, telnum[:len(node_num)])
        if node_num == telnum[:len(node_num)]:
            if len(node_num) == len(telnum):
                if len(solution) == 0 or len(node) < len(solution):
                    solution = node
            elif len(node_num) < len(telnum):
                for word in words:
                    possible_paths = [node + [word]] + possible_paths
        # print(possible_paths)

    return solution

def find_path(telnum,  words):
    """
    :param telnum:
    :param words:
    :return:
    """

    solution = []
    possible_paths = {'': {'numbers': '', 'path': [], 'num_index': 0}}

    while len(possible_paths.keys()) > 0:
        key = list(possible_paths.keys())[0]
        node = possible_paths.pop(key)
        # print(node)
        if node['numbers'] == telnum:
            if len(solution) == 0 or len(node['path']) < len(solution):
                solution = node['path']
        else:
            for word in words:
                # print(word, word_to_num(word), telnum[node['num_index']:node['num_index']+len(word)])
                if word_to_num(word) == telnum[node['num_index']:node['num_index']+len(word)]:
                    # print('Hello!')
                    if node['numbers']+word_to_num(word) not in possible_paths or len(node['path']) < len(possible_paths[node['numbers']+word_to_num(word)]['path']):
                        possible_paths[node['numbers']+word_to_num(word)] = {'numbers': node['numbers']+word_to_num(word), 'path': node['path'] + [word], 'num_index':node['num_index']+len(word)}
                # print(possible_paths)
    return solution


index = 0
lines = stdin.read().split()
while lines[index] != '-1':
    telnum = lines[index].strip()
    word_count = int(lines[index+1])
    words = [word.strip() for word in lines[index+2:index+2+word_count]]
    index = index + 2 + word_count

    # print('\n' * 3 + '=' * 30)
    # print(telnum, words)

    solution = find_path(telnum, words)
    # print(solutions)
    if len(solution) == 0:
        stdout.write('No solution.\n')
    else:
        stdout.write(' '.join(solution) + '\n')
