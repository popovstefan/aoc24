import copy
import os
from collections import Counter
from functools import cache

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd11.txt"))[0]

puzzle_input = [int(x) for x in puzzle_input.split()]

mem_cache = {0: [1]}


@cache
def f(stone):
    if stone == 0:
        return 1
    num_digits = len(str(stone))
    if num_digits % 2 == 0:
        num_digits = int(num_digits / 2)
        x = int(str(stone)[:num_digits])
        y = int(str(stone)[-num_digits:])
        return x, y
    else:
        return stone * 2024


def p1(stones):
    blinks = 25
    for i in range(blinks):
        new_stones = []
        for stone in stones:
            if stone in mem_cache:
                memoed = mem_cache[stone]
                for memo in memoed:
                    new_stones.append(memo)
            else:
                num_digits = len(str(stone))
                if num_digits % 2 == 0:
                    num_digits = int(num_digits / 2)
                    x = int(str(stone)[:num_digits])
                    y = int(str(stone)[-num_digits:])
                    new_stones.append(x)
                    new_stones.append(y)
                    mem_cache[stone] = [x, y]
                else:
                    x = stone * 2024
                    mem_cache[stone] = [x]
                    new_stones.append(x)
        stones = copy.deepcopy(new_stones)
        print("iter", i, len(stones))
    print(len(stones))


def p2(stones):
    blinks = 75
    stones = Counter(stones)
    for i in range(blinks):
        new_stones = {}
        for stone, num_stones in stones.items():
            memoed = f(stone)
            if isinstance(memoed, int):
                if memoed not in new_stones:
                    new_stones[memoed] = 0
                new_stones[memoed] += num_stones
            else:
                for memo in [memoed[0], memoed[1]]:
                    if memo not in new_stones:
                        new_stones[memo] = 0
                    new_stones[memo] += num_stones
        stones = Counter(new_stones)
    print(sum(stones.values()))


p2(puzzle_input)
