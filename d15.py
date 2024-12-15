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
    x, y = rbt
    if mv == '^':
        # check if there's at least one free cell top
        for i in range(x):
            if grd[i][y] == '.':
                tmp = grd[i][y]  # this should be free cell
                # move up everything between the 'tmp' cell and the robot position
                for k in range(i, x):
                    grd[k][y] = grd[k + 1][y]
                # free up the robot spot
                grd[x][y] = tmp
                # move the robot
                rbt = (x - 1, y)
                print(grd[x - 1][y], "robot")
                break
    elif mv == '>':
        # check if there's at least one free cell right
        for i in range(y, M):
            if grd[x][i] == '.':
                tmp = grd[x][i]  # this should be free cell
                # move right everything between the 'tmp' cell and the robot position
                for k in range(i, y, -1):
                    grd[x][k] = grd[x][k - 1]
                # free up the robot spot
                grd[x][y] = tmp
                # move the robot
                rbt = (x, y + 1)
                print(grd[x][y + 1], "robot")
                break
    elif mv == '<':
        # check if there's at least one free cell left
        for i in range(y, 0, -1):
            if grd[x][i] == '.':
                tmp = grd[x][i]  # this should be free cell
                # move left everything between the 'tmp' cell and the robot position
                for k in range(i, y):
                    grd[x][k] = grd[x][k + 1]
                # free up the robot spot
                grd[x][y] = tmp
                # move the robot
                rbt = (x, y - 1)
                print(grd[x][y - 1], "robot")
                break
    elif mv == 'v':
        # check if there's at least one free cell top
        for i in range(x, N):
            if grd[i][y] == '.':
                tmp = grd[i][y]  # this should be free cell
                # move down everything between the 'tmp' cell and the robot position
                for k in range(i, x, -1):
                    grd[k][y] = grd[k - 1][y]
                # free up the robot spot
                grd[x][y] = tmp
                # move the robot
                rbt = (x + 1, y)
                print(grd[x + 1][y], "robot")
                break
    else:
        # for weird, unsupported movements
        return rbt, grd
    # final call, return the (possibly) modified arguments
    return rbt, grd


def p1(robot_, grid_):
    for itr, movement in enumerate(movements):
        if can_move(movement, robot_, grid_):
            print(itr, "moving", movement, robot_)
            robot_, grid_ = move(movement, robot_, grid_)

    result = 0
    for i in range(N):
        for j in range(M):
            if grid_[i][j] == 'O':
                result += (i * 100 + j)
    print(result)


p1(robot, grid)
