import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd9.txt"))
# it's just one line
puzzle_input = puzzle_input[0]

print(puzzle_input)


def p1():
    disk = []
    n = len(puzzle_input)
    i = 1
    order = 0
    num_dots = 0
    free = '.'
    while i <= n:
        if i % 2:
            file = int(puzzle_input[i - 1])
            for x in range(file):
                disk.append(order)
            order += 1
        else:
            free_space = int(puzzle_input[i - 1])
            for x in range(free_space):
                disk.append(free)
                num_dots += 1
        i += 1
    print(disk)
    print(num_dots)
    fixed_disk = [free] * num_dots
    iters = 0
    i = 0
    j = len(disk) - 1
    while iters < num_dots and disk[-num_dots:] != fixed_disk:
        while disk[i] != free:
            i += 1
        while disk[j] == free:
            j -= 1
        tmp = disk[i]
        disk[i] = disk[j]
        disk[j] = tmp

    i = 0
    result = 0
    while disk[i] != free:
        result += i * int(disk[i])
        i += 1

    print(result)


def p2():
    disk = []
    n = len(puzzle_input)
    i = 1
    order = 0
    num_dots = 0
    free = '.'
    while i <= n:
        if i % 2:
            file = int(puzzle_input[i - 1])
            for x in range(file):
                disk.append(order)
            order += 1
        else:
            free_space = int(puzzle_input[i - 1])
            for x in range(free_space):
                disk.append(free)
                num_dots += 1
        i += 1
    j = len(disk) - 1
    while j >= 0:
        while disk[j] == free:
            j -= 1
        curr_id = int(disk[j])
        sj = j
        kj = 0
        while disk[sj] != free and int(disk[sj]) == curr_id:
            sj -= 1
            kj += 1
        i = 0
        ki = 0
        while i < j:
            if disk[i] != free:
                ki = 0
            else:
                ki += 1
                if ki == kj:
                    break
            i += 1
        # print(ki, kj, sj, i, j)
        if i >= j:
            while j >= 0 and disk[j] != free and int(disk[j]) == curr_id:
                j -= 1
            continue
        for p in range(kj):
            # print("sw", disk[i + p], disk[j - p])
            tmp = disk[i - p]
            disk[i - p] = disk[j - p]
            disk[j - p] = tmp

    i = 0
    result = 0
    print(disk)
    while i < len(disk):
        if disk[i] != free:
            result += i * int(disk[i])
        i += 1

    print(result)


p2()
