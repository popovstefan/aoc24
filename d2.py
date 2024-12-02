import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd2.txt"))

def p1():
    solution = 0
    for line in puzzle_input:
        elements = [int(x) for x in line.split()]
        increase = 0
        decrease = 0
        big_diff = 0
        problem_dampener = 0
        # print(elements)
        for inx, current in enumerate(elements[1:]):
            previous = elements[inx]
            diff = abs(current - previous)
            # print(current, previous, diff)
            if diff > 3 or diff < 1:
                big_diff += 1
                break
            if current > previous:
                increase += 1
            if current < previous:
                decrease += 1
            if increase > 0 and decrease > 0:
                break
        if (increase > 0 and decrease > 0) or big_diff > 0:
            continue
        else:
            solution += 1
    print(solution)

p1()



