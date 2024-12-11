import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd10.txt"))

env = []
for i, row in enumerate(puzzle_input):
    env.append([])
    for j, col in enumerate(row):
        env[i].append(int(col))

print(env)

n = len(env)
m = len(env[0])


def p1():
    def hike(x, y, val, trail):
        if val == 9:
            trail.add((x, y))
            return
        # check top
        if x > 0 and env[x - 1][y] == val + 1:
            hike(x - 1, y, val + 1, trail)
        # check bottom
        if x < n - 1 and env[x + 1][y] == val + 1:
            hike(x + 1, y, val + 1, trail)
        # check left
        if y > 0 and env[x][y - 1] == val + 1:
            hike(x, y - 1, val + 1, trail)
        # check right
        if y < m - 1 and env[x][y + 1] == val + 1:
            hike(x, y + 1, val + 1, trail)

    result = 0
    for i, r in enumerate(env):
        for j, c in enumerate(r):
            if c == 0:
                t = set()
                hike(i, j, c, t)
                result += len(t)
    print(result)


def p2():
    def hike(x, y, val, trail):
        if val == 9:
            trail.append((x, y))
            return
        # check top
        if x > 0 and env[x - 1][y] == val + 1:
            hike(x - 1, y, val + 1, trail)
        # check bottom
        if x < n - 1 and env[x + 1][y] == val + 1:
            hike(x + 1, y, val + 1, trail)
        # check left
        if y > 0 and env[x][y - 1] == val + 1:
            hike(x, y - 1, val + 1, trail)
        # check right
        if y < m - 1 and env[x][y + 1] == val + 1:
            hike(x, y + 1, val + 1, trail)

    result = 0
    for i, r in enumerate(env):
        for j, c in enumerate(r):
            if c == 0:
                t = []
                hike(i, j, c, t)
                result += len(t)
    print(result)


p2()
