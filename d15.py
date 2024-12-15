import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd15.txt"))

grid = []
movements = []

for i, line in enumerate(puzzle_input):
    if line.strip() == "":
        continue
    if line.startswith("#"):
        grid.append([])
        for char in line:
            grid[i].append(char)
    else:
        for char in line:
            movements.append(char)


print(grid)
print(movements)