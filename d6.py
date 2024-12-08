import collections
import os
import time

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
    ordered = []
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
                        if (x - 1, y) not in seen:
                            ordered.append((x - 1, y))
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
                        if (x, y + 1) not in seen:
                            ordered.append((x, y + 1))
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
                        if (x + 1, y) not in seen:
                            ordered.append((x + 1, y))
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
                        if (x, y - 1) not in seen:
                            ordered.append((x, y - 1))
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
    seen.remove(guard)
    print(len(seen))
    return ordered


def p2(p1seen: set):
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
    loop_candidates = []
    for inx in range(n):
        for jnx in range(m):
            if puzzle_input[inx][jnx] != clear and puzzle_input[inx][jnx] != wall:
                guard = (inx, jnx, '^')
            if puzzle_input[inx][jnx] == clear and (inx, jnx) in set(p1seen):  # any clear point is a potential loop candidate
                loop_candidates.append((inx, jnx, wall))

    lcs = len(loop_candidates)
    num_loops = 0
    e = 0

    for i, loop_candidate in enumerate(loop_candidates):
        # print(i, "of", lcs)
        this_puzzle_input = [x[:] for x in puzzle_input]
        # put an obstacle, check for loop
        this_puzzle_input[loop_candidate[0]][loop_candidate[1]] = wall
        # run the guard through the maze with the loop put
        queue = collections.deque()
        queue.append(guard)
        seen = {guard}
        loop_detected = False
        tick = time.time()
        while queue:
            if time.time() - tick > 0.2:
                num_loops += 1
                break
            path = queue.popleft()
            x, y, dr = path
            # if the guard has left the maze, break away
            if x >= n or x < 0 or y < 0 or y >= m:
                break
            # try to move one place
            try:
                while True:
                    if time.time() - tick > 0.2:
                        num_loops += 1
                        break
                    if this_puzzle_input[x][y] == '^':  # top
                        if this_puzzle_input[x - 1][y] == clear:
                            # clean current place
                            this_puzzle_input[x][y] = clear
                            # move the guard
                            this_puzzle_input[x - 1][y] = '^'
                            # add the new place to the queue
                            queue.append((x - 1, y, '^'))
                            break
                        else:
                            # mark it as seen
                            if (x - 1, y, '^') in seen:
                                loop_detected = True
                                break
                            seen.add((x - 1, y, '^'))
                            this_puzzle_input[x][y] = go_right[this_puzzle_input[x][y]]
                    if this_puzzle_input[x][y] == '>':  # right
                        if this_puzzle_input[x][y + 1] == clear:
                            # clean current place
                            this_puzzle_input[x][y] = clear
                            # move the guard
                            this_puzzle_input[x][y + 1] = '>'
                            # add the new place to the queue
                            queue.append((x, y + 1, '>'))
                            break
                        else:
                            # mark it as seen
                            if (x, y + 1, '>') in seen:
                                loop_detected = True
                                break
                            seen.add((x, y + 1, '>'))
                            this_puzzle_input[x][y] = go_right[this_puzzle_input[x][y]]
                    if this_puzzle_input[x][y] == 'v':  # bottom
                        if this_puzzle_input[x + 1][y] == clear:
                            # clean current place
                            this_puzzle_input[x][y] = clear
                            # move the guard
                            this_puzzle_input[x + 1][y] = 'v'
                            # add the new place to the queue
                            queue.append((x + 1, y, 'v'))
                            break
                        else:
                            # mark it as seen
                            if (x + 1, y, 'v') in seen:
                                loop_detected = True
                                break
                            seen.add((x + 1, y, 'v'))
                            this_puzzle_input[x][y] = go_right[this_puzzle_input[x][y]]
                    if this_puzzle_input[x][y] == '<':  # left
                        if this_puzzle_input[x][y - 1] == clear:
                            # clean current place
                            this_puzzle_input[x][y] = clear
                            # move the guard
                            this_puzzle_input[x][y - 1] = '<'
                            # add the new place to the queue
                            queue.append((x, y - 1, '<'))
                            break
                        else:
                            # mark it as seen
                            if (x, y - 1, '<') in seen:
                                loop_detected = True
                                break
                            seen.add((x, y - 1, '<'))
                            this_puzzle_input[x][y] = go_right[this_puzzle_input[x][y]]
            except IndexError:
                # index out of bounds, anywhere means guard has left the board
                e += 1
            if loop_detected:
                num_loops += 1
                break
    print(num_loops)
    # print(e)


seenp1 = p1()
p2(seenp1)
