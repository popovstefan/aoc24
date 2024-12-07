import collections
import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd6.txt"))

# convert to matrix of chars
puzzle_input = [list(i + ' ' * (len(max(puzzle_input)) - len(i))) for i in puzzle_input]


def p1():
    clear = '.'
    wall = '#'

    go_right = {
        'v': '<',
        '<': '^',
        '^': '>',
        '>': 'v'
    }

    n, m = len(puzzle_input), len(puzzle_input[0])
    guard = ()
    for inx in range(n):
        for jnx in range(m):
            if puzzle_input[inx][jnx] != clear and puzzle_input[inx][jnx] != wall:
                guard = (inx, jnx)
                break
    print(guard)
    queue = collections.deque()
    queue.append(guard)
    seen = {guard}
    while queue:
        path = queue.popleft()
        x, y = path
        # if the guard has left the maze, break away
        if x >= n or x < 0 or y < 0 or y >= m:
            break
        # try to move one place
        try:
            while True:
                if puzzle_input[x][y] == '^':  # top
                    if puzzle_input[x - 1][y] == clear:
                        # clean current place
                        puzzle_input[x][y] = clear
                        # move the guard
                        puzzle_input[x - 1][y] = '^'
                        # mark it as seen
                        seen.add((x - 1, y))
                        # add the new place to the queue
                        queue.append((x - 1, y))
                        print(x - 1, y)
                        break
                    else:
                        puzzle_input[x][y] = go_right[puzzle_input[x][y]]
                if puzzle_input[x][y] == '>':  # right
                    if puzzle_input[x][y + 1] == clear:
                        # clean current place
                        puzzle_input[x][y] = clear
                        # move the guard
                        puzzle_input[x][y + 1] = '>'
                        # mark it as seen
                        seen.add((x, y + 1))
                        # add the new place to the queue
                        queue.append((x, y + 1))
                        print(x, y + 1)
                        break
                    else:
                        puzzle_input[x][y] = go_right[puzzle_input[x][y]]
                if puzzle_input[x][y] == 'v':  # bottom
                    if puzzle_input[x + 1][y] == clear:
                        # clean current place
                        puzzle_input[x][y] = clear
                        # move the guard
                        puzzle_input[x + 1][y] = 'v'
                        # mark it as seen
                        seen.add((x + 1, y))
                        # add the new place to the queue
                        queue.append((x + 1, y))
                        print(x + 1, y)
                        break
                    else:
                        puzzle_input[x][y] = go_right[puzzle_input[x][y]]
                if puzzle_input[x][y] == '<':  # left
                    if puzzle_input[x][y - 1] == clear:
                        # clean current place
                        puzzle_input[x][y] = clear
                        # move the guard
                        puzzle_input[x][y - 1] = '<'
                        # mark it as seen
                        seen.add((x, y - 1))
                        # add the new place to the queue
                        queue.append((x, y - 1))
                        print(x, y - 1)
                        break
                    else:
                        puzzle_input[x][y] = go_right[puzzle_input[x][y]]
        except IndexError:
            # index out of bounds, anywhere
            print(len(seen))
    print(len(seen) - 1)


def p2():
    clear = '.'
    wall = '#'

    go_right = {
        'v': '<',
        '<': '^',
        '^': '>',
        '>': 'v'
    }

    n, m = len(puzzle_input), len(puzzle_input[0])
    guard = ()
    for inx in range(n):
        for jnx in range(m):
            if puzzle_input[inx][jnx] != clear and puzzle_input[inx][jnx] != wall:
                guard = (inx, jnx)
                break
    print(guard)
    queue = collections.deque()
    queue.append(guard)
    seen = {guard}
    loops = {}
    while queue:
        path = queue.popleft()
        x, y = path
        # if the guard has left the maze, break away
        if x >= n or x < 0 or y < 0 or y >= m:
            break
        # try to move one place
        try:
            while True:
                if puzzle_input[x][y] == '^':  # top
                    if puzzle_input[x - 1][y] == clear:
                        # clean current place
                        puzzle_input[x][y] = clear
                        # move the guard
                        puzzle_input[x - 1][y] = '^'
                        # mark it as seen
                        if (x - 1, y) in seen:
                            loops[(x, y)] = 1
                        seen.add((x - 1, y))
                        # add the new place to the queue
                        queue.append((x - 1, y))
                        print(x - 1, y)
                        break
                    else:
                        puzzle_input[x][y] = go_right[puzzle_input[x][y]]
                if puzzle_input[x][y] == '>':  # right
                    if puzzle_input[x][y + 1] == clear:
                        # clean current place
                        puzzle_input[x][y] = clear
                        # move the guard
                        puzzle_input[x][y + 1] = '>'
                        # mark it as seen
                        if (x, y + 1) in seen:
                            loops[(x, y)] = 1
                        seen.add((x, y + 1))
                        # add the new place to the queue
                        queue.append((x, y + 1))
                        print(x, y + 1)
                        break
                    else:
                        puzzle_input[x][y] = go_right[puzzle_input[x][y]]
                if puzzle_input[x][y] == 'v':  # bottom
                    if puzzle_input[x + 1][y] == clear:
                        # clean current place
                        puzzle_input[x][y] = clear
                        # move the guard
                        puzzle_input[x + 1][y] = 'v'
                        # mark it as seen
                        if (x + 1, y) in seen:
                            loops[(x, y)] = 1
                        seen.add((x + 1, y))
                        # add the new place to the queue
                        queue.append((x + 1, y))
                        print(x + 1, y)
                        break
                    else:
                        puzzle_input[x][y] = go_right[puzzle_input[x][y]]
                if puzzle_input[x][y] == '<':  # left
                    if puzzle_input[x][y - 1] == clear:
                        # clean current place
                        puzzle_input[x][y] = clear
                        # move the guard
                        puzzle_input[x][y - 1] = '<'
                        # mark it as seen
                        if (x, y - 1) in seen:
                            loops[(x, y)] = 1
                        seen.add((x, y - 1))
                        # add the new place to the queue
                        queue.append((x, y - 1))
                        print(x, y - 1)
                        break
                    else:
                        puzzle_input[x][y] = go_right[puzzle_input[x][y]]
        except IndexError:
            # index out of bounds, anywhere
            print(len(seen))
            print(len(loops))
    # print(len(seen) - 1)
    # print(len(loops))


p2()