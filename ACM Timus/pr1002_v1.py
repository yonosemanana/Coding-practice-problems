### Site: https://acm.timus.ru/
### Problem: 1002

### Failed on Test 4

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

    solutions = []
    possible_paths = [[word] for word in words]

    while len(possible_paths) > 0:
        node = possible_paths.pop(0)
        node_str = ''.join(node)
        node_num = word_to_num(node_str)

        # print(node, node_str, node_num, telnum[:len(node_num)])
        if node_num == telnum[:len(node_num)]:
            if len(node_num) == len(telnum):
                solutions.append(node)
            elif len(node_num) < len(telnum):
                for word in words:
                    possible_paths = [node + [word]] + possible_paths
        # print(possible_paths)

    return solutions

index = 0
lines = stdin.read().split()
while lines[index] != '-1':
    telnum = lines[index].strip()
    word_count = int(lines[index+1])
    words = sorted([word.strip() for word in lines[index+2:index+2+word_count]], key = lambda x: len(x))
    index = index + 2 + word_count

    # print('\n' * 3 + '=' * 30)
    solutions = search_words(telnum, words)
    # print(solutions)
    if len(solutions) == 0:
        stdout.write('No solution.\n')
    else:
        solution = min(solutions, key = lambda x: len(x))
        stdout.write(' '.join(solution) + '\n')
