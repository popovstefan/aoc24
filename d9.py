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
    while i <= n:
        if i % 2:
            file = int(puzzle_input[i - 1])
            for x in range(file):
                disk.append(order)
            order += 1
        else:
            free_space = int(puzzle_input[i - 1])
            for x in range(free_space):
                disk.append('.')
        i += 1
    copy_disk = [x for x in disk]
    copy_reversed = [x for x in disk]
    copy_reversed = copy_reversed[::-1]

    def numbers_left(arr, inx):
        return any([str(x).isdigit() for x in arr[inx:]])

    def find_first(arr, inx):
        pass

    j = 0
    for i in range(len(copy_disk)):
        if copy_disk[i] == '.' and numbers_left(copy_disk, i) > 0:
            first = find_first(copy_reversed, j)
            if first is None:
                break
            copy_disk[i] = first
            j += 1

    print(copy_disk)


p1()
