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


def p2():
    left = []
    right = []
    for row in puzzle_input:
        elements = row.split()
        left.append(int(elements[0]))
        right.append(int(elements[1]))

    similarities = {}
    for el in left:
        if el not in similarities:
            similarities[el] = (el * right.count(el))
        else:
            similarities[el] += (el * right.count(el))

    solution = sum(similarities.values())
    print(solution)

p2()