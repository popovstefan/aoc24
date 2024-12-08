import os
from itertools import combinations

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd8.txt"))

antennae = {}

n = len(puzzle_input)
m = len(puzzle_input[0])

for i, line in enumerate(puzzle_input):
    for j, char in enumerate(line):
        if char != '.':
            if char not in antennae:
                antennae[char] = set()
            antennae[char].add((i, j))


# print(n, m)
# print(antennae)


def p1(anteni: dict, antipodes: set):
    for k, v in anteni.items():
        # print(k)
        for combo in combinations(v, 2):
            x, y = combo
            # print(x, y)
            ap = (x[0] - (y[0] - x[0]), x[1] - (y[1] - x[1]))
            # print(ap)
            if 0 <= ap[0] < n and 0 <= ap[1] < m:
                antipodes.add(ap)
            ap = (y[0] + (y[0] - x[0]), y[1] + (y[1] - x[1]))
            # print(ap)
            if 0 <= ap[0] < n and 0 <= ap[1] < m:
                antipodes.add(ap)

    print(len(antipodes))


def p2():
    antipodes = set()
    for k, v in antennae.items():
        # print(k)
        for combo in combinations(v, 2):
            x, y = combo
            # print(x, y)
            for i in range(n):
                ap = (x[0] - i * (y[0] - x[0]), x[1] - i * (y[1] - x[1]))
                if 0 <= ap[0] < n and 0 <= ap[1] < m:
                    print(ap)
                    antipodes.add(ap)
                ap = (y[0] + i * (y[0] - x[0]), y[1] + i * (y[1] - x[1]))
                if 0 <= ap[0] < n and 0 <= ap[1] < m:
                    antipodes.add(ap)
        # break
    print(len(antipodes))


p2()
