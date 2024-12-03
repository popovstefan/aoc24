import os
from os import remove

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
        for inx, current in enumerate(elements[1:]):
            previous = elements[inx]
            diff = abs(current - previous)
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





def p2():
    def is_safe(numbers: list[int], problem_dampener: bool = False, remove_first: bool = True):
        if len(set(numbers)) == 1:
            return False
        inc = 0
        dec = 0
        bd = 0
        eqs = 0
        pp = -1
        for i, curr in enumerate(numbers):
            nxt_i = min(len(numbers) - 1, i + 1)
            if nxt_i == i:
                break
            nxt = elements[nxt_i]
            df = abs(curr - nxt)
            if df > 3 or df < 1:
                bd += 1
                pp = i
                break
            if curr > nxt:
                inc += 1
            elif curr < nxt:
                dec += 1
            else:
                eqs += 1
            if inc > 0 and dec > 0:
                pp = i
                break
        if (inc > 0 and dec > 0) or bd > 0 or eqs > 1:
            if problem_dampener:
                return False
            else:
                if remove_first:
                    numbers.pop(pp)
                else:
                    numbers.pop(pp + 1)
                return is_safe(numbers, True)
        else:
            return True

    solution = 0
    for line in puzzle_input:
        elements = [int(x) for x in line.split()]
        if is_safe(elements, False, False):
            solution += 1
        elif is_safe(elements, False, True):
            solution += 1
        elif is_safe(elements[1:], True, True):
            print(line)
            solution += 1
        elif is_safe(elements[1:], True, False):
            solution += 1
        elif is_safe(elements[:-1], True, True):
            solution += 1
        elif is_safe(elements[:-1], True, False):
            solution += 1
        # else:
        #     print(line)
    print(solution)


p2()
