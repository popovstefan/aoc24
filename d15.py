import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd15.txt"))


def read_elements(p):
    g = []
    r = None
    moves = []

    for i, line in enumerate(p):
        if line.strip() == "":
            continue
        if line.startswith("#"):
            g.append([])
            for j, char in enumerate(line):
                if char == '@':
                    r = (i, j)
                g[i].append(char)
        else:
            for char in line:
                moves.append(char)
    return g, r, moves, len(g), len(g[0])


grid, robot, movements, N, M = read_elements(puzzle_input)


def can_move(mv, rbt, grd):
    x, y = rbt
    if mv == '^':
        # check if there's at least one free cell top
        for i in range(x):
            if grd[i][y] == '.':
                return True
    elif mv == '>':
        # check if there's at least one free cell right
        for i in range(y, M):
            if grd[x][i] == '.':
                return True
    elif mv == '<':
        # check if there's at least one free cell left
        for i in range(y):
            if grd[x][i] == '.':
                return True
    elif mv == 'v':
        # check if there's at least one free cell top
        for i in range(x, N):
            if grd[i][y] == '.':
                return True
    else:
        # for weird, unsupported movements
        return False
    # default, return no free cells
    return False


def move(mv, rbt, grd):
    return rbt, grd


def p1(robot_, grid_):
    for itr, movement in enumerate(movements):
        if can_move(movement, robot_, grid_):
            print(itr, "moving", robot_)
            robot_, grid_ = move(movement, robot_, grid_)

    result = 0
    for i in range(N):
        for j in range(M):
            if grid_[i][j] == 'O':
                result += (i * 100 + j)
    print(result)


p1(robot, grid)
