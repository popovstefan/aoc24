import os
import re
from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd3.txt"))

def p1():
    solution = 0
    for line in puzzle_input:
        muls = re.findall(pattern=r"mul\(\d{1,3},\d{1,3}\)", string=line)
        for mul in muls:
            numbers = re.findall(pattern="\d+", string=mul)
            numbers = [int(number) for number in numbers]
            solution += (numbers[0] * numbers[1])
    print(solution)

def p2():
    solution = 0
    enabled = True
    for line in puzzle_input:
        matches = re.findall(pattern=r"(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))", string=line)
        for match in matches:
            if match == "don't()":
                enabled = False
                continue
            if match == "do()":
                enabled = True
                continue
            if match.startswith("mul(") and enabled:
                numbers = re.findall(pattern="\d+", string=match)
                numbers = [int(number) for number in numbers]
                solution += (numbers[0] * numbers[1])
    print(solution)

p2()