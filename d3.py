import os
import re
from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd3.txt"))

solution = 0
for line in puzzle_input:
    muls = re.findall(pattern=r"mul\(\d{1,3},\d{1,3}\)", string=line)
    for mul in muls:
        numbers = re.findall(pattern="\d+", string=mul)
        numbers = [int(number) for number in numbers]
        solution += (numbers[0] * numbers[1])
print(solution)