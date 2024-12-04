import os
import numpy as np
from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd4.txt"))


def p1(pi):
    def count_occurrences(swr):
        result = 0
        for sw in swr:
            # check main diagonal
            diag = "".join(np.diag(sw, 0))
            if diag == "XMAS" or diag[::-1] == "XMAS":
                print(diag)
                result += 1
            # check rows and columns
            for i in range(len(diag)):
                row = "".join(sw[i, :])
                column = "".join(sw[:, i])
                if row == "XMAS" or row[::-1] == "XMAS":
                    print(row)
                    result += 1
                if column == "XMAS" or column[::-1] == "XMAS":
                    print(column)
                    result += 1
            # check side diagonal
            diag = "".join(np.diag(np.fliplr(sw), 0))
            if diag == "XMAS" or diag[::-1] == "XMAS":
                print(diag)
                result += 1
        return result

    pi = [list(i + ' ' * (len(max(pi)) - len(i))) for i in pi]

    sliding_windows = np.lib.stride_tricks.sliding_window_view(x=pi, window_shape=(4, 4))
    print(sliding_windows.shape)
    solution = 0
    for sliding_window_row in sliding_windows:
        # todo counts same occurrence multiple times, try padding
        solution += count_occurrences(sliding_window_row)

    print(solution)


p1(puzzle_input)
