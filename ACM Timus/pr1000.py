from sys import stdin, stdout

numbers = stdin.read().split()
stdout.write(str(sum([int(x) for x in numbers])))