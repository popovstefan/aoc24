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
                antennae[char] = []
            antennae[char].append((i, j))

# print(n, m)
# print(antennae)
antipodes = set()

def p1():
    for k, v in antennae.items():
        print(k)
        for combo in combinations(v, 2):
            x, y = combo
            print(x, y)
            antipode = (x[0] - (y[0] - x[0]), x[1] - (y[1] - x[1]))
            print(antipode)
            if 0 <= antipode[0] < n and 0 <= antipode[1] < m:
                antipodes.add(antipode)
            antipode = (y[0] + (y[0] - x[0]), y[1] + (y[1] - x[1]))
            print(antipode)
            if 0 <= antipode[0] < n and 0 <= antipode[1] < m:
                antipodes.add(antipode)

    print(len(antipodes))


def p2():
    pass


p1()
