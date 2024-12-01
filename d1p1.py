import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd1.txt"))


def p1():
    left = []
    right = []
    for row in puzzle_input:
        elements = row.split()
        left.append(int(elements[0]))
        right.append(int(elements[1]))

    left = sorted(left)
    right = sorted(right)

    solution = sum([abs(x[0] - x[1]) for x in zip(left ,right)])
    print(solution)
    