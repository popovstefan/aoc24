import os

import numpy as np

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd13.txt"))

claws = []


def p1():
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0
    c1 = 0
    c2 = 0
    for line in puzzle_input:
        if line.startswith("Button A:"):
            parts = line.split(":")
            parts = parts[1].split(", ")
            x = parts[0].index("X") + 1
            y = parts[1].index("Y") + 1
            a1 = int(parts[0][x:])
            a2 = int(parts[1][y:])
        if line.startswith("Button B:"):
            parts = line.split(":")
            parts = parts[1].split(", ")
            x = parts[0].index("X") + 1
            y = parts[1].index("Y") + 1
            b1 = int(parts[0][x:])
            b2 = int(parts[1][y:])
        if line.startswith("Prize:"):
            parts = line.split(":")
            parts = parts[1].split(", ")
            x = parts[0].index("X") + 2
            y = parts[1].index("Y") + 2
            c1 = int(parts[0][x:])
            c2 = int(parts[1][y:])
        if len(line.strip()) == 0:
            claws.append([a1, a2, b1, b2, c1, c2])
            a1 = 0
            a2 = 0
            b1 = 0
            b2 = 0
            c1 = 0
            c2 = 0
    result = 0
    for claw in claws:
        print(claw)
        a1, a2, b1, b2, c1, c2 = claw
        delta = (b2 * a1) - (a2 * b1)
        if delta == 0:
            # infinite solutions
            continue
        else:
            delta_x = (c1 * b2) - (b1 * c2)
            delta_y = (a1 * c2) - (c1 * a2)
            x = delta_x / delta
            y = delta_y / delta
            if np.isclose(x, int(x)) and np.isclose(y, int(y)):
                print(delta, delta_x, delta_y)
                x = int(x)
                y = int(y)
                print(x, y)
                if x < 100 and y < 100:
                    result += (3 * x + y)
    print(result)


def p2():
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0
    c1 = 0
    c2 = 0
    for line in puzzle_input:
        if line.startswith("Button A:"):
            parts = line.split(":")
            parts = parts[1].split(", ")
            x = parts[0].index("X") + 1
            y = parts[1].index("Y") + 1
            a1 = int(parts[0][x:])
            a2 = int(parts[1][y:])
        if line.startswith("Button B:"):
            parts = line.split(":")
            parts = parts[1].split(", ")
            x = parts[0].index("X") + 1
            y = parts[1].index("Y") + 1
            b1 = int(parts[0][x:])
            b2 = int(parts[1][y:])
        if line.startswith("Prize:"):
            parts = line.split(":")
            parts = parts[1].split(", ")
            x = parts[0].index("X") + 2
            y = parts[1].index("Y") + 2
            c1 = int(parts[0][x:]) + 10000000000000
            c2 = int(parts[1][y:]) + 10000000000000
        if len(line.strip()) == 0:
            claws.append([a1, a2, b1, b2, c1, c2])
            a1 = 0
            a2 = 0
            b1 = 0
            b2 = 0
            c1 = 0
            c2 = 0
    result = 0
    print(claws)
    for claw in claws:
        a1, a2, b1, b2, c1, c2 = claw
        delta = (b2 * a1) - (a2 * b1)
        if delta == 0:
            # infinite solutions
            continue
        else:
            delta_x = (c1 * b2) - (b1 * c2)
            delta_y = (a1 * c2) - (c1 * a2)
            if delta_x / delta == delta_x // delta and delta_y / delta == delta_y // delta:
                x = delta_x / delta
                y = delta_y / delta
                x = int(x)
                y = int(y)
                # if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2:
                print(claw)
                print(delta, delta_x, delta_y)
                print(x, y)
                result += (3 * x + y)
    print(result)


p2()
