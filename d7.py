import os
from itertools import product
from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd7.txt"))


def p1():
    solution = 0
    for line in puzzle_input:
        parts = line.split(":")
        eq_res = int(parts[0])
        eq = parts[1].split()
        eq_numbers = []
        for eq_el in eq:
            eq_numbers.append(int(eq_el.strip()))
        print(eq_res, eq_numbers)

        combos = [''.join(map(str, i)) for i in product([0, 1], repeat=len(eq_numbers) - 1)]
        for combo in combos:
            combo_res = eq_numbers[0]
            for i, char in enumerate(combo):
                if char == '0':
                    combo_res += eq_numbers[i + 1]
                else:
                    combo_res *= eq_numbers[i + 1]
                # if combo_res >= eq_res:
                #     break
            if combo_res == eq_res:
                print("adding", combo_res)
                solution += eq_res
                break
    print(solution)


def p2():
    solution = 0
    for line in puzzle_input:
        parts = line.split(":")
        eq_res = int(parts[0])
        eq = parts[1].split()
        eq_numbers = []
        for eq_el in eq:
            eq_numbers.append(int(eq_el.strip()))
        print(eq_res, eq_numbers)

        combos = [''.join(map(str, i)) for i in product([0, 1, 2], repeat=len(eq_numbers) - 1)]
        for combo in combos:
            combo_res = eq_numbers[0]
            n = len(combo)
            i = 0
            while i < n:
                char = combo[i]
                if char == '0':
                    combo_res += eq_numbers[i + 1]
                elif char == '1':
                    combo_res *= eq_numbers[i + 1]
                else:
                    combo_res = int(str(combo_res) + str(eq_numbers[i + 1]))
                i += 1
                # if combo_res >= eq_res:
                #     break
            if combo_res == eq_res:
                print("adding", combo_res)
                solution += eq_res
                break
    print(solution)


p2()
