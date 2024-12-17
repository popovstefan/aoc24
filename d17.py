import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd17.txt"))

print(puzzle_input)

rega = int(puzzle_input[0].split("Register A:")[1].strip())
regb = int(puzzle_input[1].split("Register B:")[1].strip())
regc = int(puzzle_input[2].split("Register C:")[1].strip())

prgrm = [int(x.strip()) for x in puzzle_input[4].split("Program:")[1].split(",")]

print(rega, regb, regc)
print(prgrm)