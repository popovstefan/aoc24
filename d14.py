import os
from functools import cache

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd14.txt"))

robots = []

for line in puzzle_input:
    parts = line.split()
    position = parts[0].split(",")
    x = int(position[0].strip()[2:])
    y = int(position[1].strip())
    velocity = parts[1].split(",")
    vx = int(velocity[0].strip()[2:])
    vy = int(velocity[1].strip())
    print(position, x, y, velocity, vx, vy)
    robots.append((x, y, vx, vy))

n = 101
m = 103


@cache
def move_robot(x_, y_, dx_, dy_):
    return (x_ + dx_) % n, (y_ + dy_) % m


def p1(my_robots):
    seconds = 132
    env = {}
    for robot in my_robots:
        x, y, dx, dy = robot
        new_x = (x + (dx * seconds)) % n
        new_y = (y + (dy * seconds)) % m
        if (new_x, new_y) not in env:
            env[(new_x, new_y)] = 0
        env[(new_x, new_y)] += 1
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for k, v in env.items():
        x, y = k
        if v > 0:
            if x < n // 2 and y < m // 2:
                q1 += v
            if x > n // 2 and y > m // 2:
                q4 += v
            if x < n // 2 and y > m // 2:
                q3 += v
            if x > n // 2 and y < m // 2:
                q2 += v

    print(q1, q2, q3, q4)
    print(q1 * q2 * q3 * q4)


def p2(my_robots):
    res = []
    for seconds in range(1, 101 * 103):
        env = {}
        for robot in my_robots:
            x, y, dx, dy = robot
            new_x = (x + (dx * seconds)) % n
            new_y = (y + (dy * seconds)) % m
            if (new_x, new_y) not in env:
                env[(new_x, new_y)] = 0
            env[(new_x, new_y)] += 1
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        for k, v in env.items():
            x, y = k
            if v > 0:
                if x < n // 2 and y < m // 2:
                    q1 += v
                if x > n // 2 and y > m // 2:
                    q4 += v
                if x < n // 2 and y > m // 2:
                    q3 += v
                if x > n // 2 and y < m // 2:
                    q2 += v

        # print(q1, q2, q3, q4)
        # print(q1 * q2 * q3 * q4)
        res.append((seconds, q1 * q2 * q3 * q4))
    print(sorted(res, key=lambda x: x[1])[:15])


p2(robots)
