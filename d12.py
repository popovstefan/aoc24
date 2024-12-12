import os
from functools import cache

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd12.txt"))

garden = []
for i, row in enumerate(puzzle_input):
    garden.append([])
    for j, col in enumerate(row):
        garden[i].append(col)

n = len(garden)
m = len(garden[0])


@cache
def perimeter(i, j):
    val = garden[i][j]
    p = 0
    # check top
    if i > 0 and garden[i - 1][j] != val:
        p += 1
    # check bottom
    if i < n - 1 and garden[i + 1][j] != val:
        p += 1
    # check left
    if j > 0 and garden[i][j - 1] != val:
        p += 1
    # check right
    if j < m - 1 and garden[i][j + 1] != val:
        p += 1
    # check boundaries
    if i == 0:
        p += 1
    if i == n - 1:
        p += 1
    if j == 0:
        p += 1
    if j == m - 1:
        p += 1
    return p


@cache
def perimeter2(i, j):
    val = garden[i][j]
    p = set()
    # check top
    if i > 0 and garden[i - 1][j] != val:
        p.add((i - 1, j))
    # check bottom
    if i < n - 1 and garden[i + 1][j] != val:
        p.add((i + 1, j))
    # check left
    if j > 0 and garden[i][j - 1] != val:
        p.add((i, j - 1))
    # check right
    if j < m - 1 and garden[i][j + 1] != val:
        p.add((i, j + 1))
    # check boundaries
    if i == 0:
        p.add((i - 1, j))
    if i == n - 1:
        p.add((i + 1, j))
    if j == 0:
        p.add((i, j - 1))
    if j == m - 1:
        p.add((i, j + 1))
    return p


def p1():
    def make_plot(x, y, p, v):
        if garden[x][y] != v:
            return
        # check top
        if x > 0 and garden[x - 1][y] == v and (x - 1, y) not in p:
            p.add((x - 1, y))
            make_plot(x - 1, y, p, v)
            # vv.add((x - 1, y))
        # check bottom
        if x < n - 1 and garden[x + 1][y] == v and (x + 1, y) not in p:
            p.add((x + 1, y))
            make_plot(x + 1, y, p, v)
            # vv.add((x + 1, y))
        # check left
        if y > 0 and garden[x][y - 1] == v and (x, y - 1) not in p:
            p.add((x, y - 1))
            make_plot(x, y - 1, p, v)
            # vv.add((x, y - 1))
        # check right
        if y < m - 1 and garden[x][y + 1] == v and (x, y + 1) not in p:
            p.add((x, y + 1))
            make_plot(x, y + 1, p, v)
            # vv.add((x, y + 1))

    visited = set()
    plots = []
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                # visit the current field
                visited.add((i, j))
                plot = set()
                plot.add((i, j))
                # construct plot
                make_plot(i, j, plot, garden[i][j])
                # print(plot)
                # visit the entire plot
                visited = visited.union(plot)
                # add the plot
                plots.append(plot)
            # print("visited", visited)
    result = 0
    for plot in plots:
        a = 0
        p = 0
        for el in plot:
            p += perimeter(el[0], el[1])
            a += 1
        result += (a * p)
        print(plot)
        # print(a, p, plot)
        # print(result)
    print(result)
    # print(len(plots))


def p2():
    def check_perimeter(x, y, v):
        fs = set()
        # check top + boundary
        if (x == 0) or (x > 0 and garden[x - 1][y] != v):
            fs.add((x - 1, y))
            # fs.add((x - 0.5, y))
        # check bottom + boundary
        if (x == n - 1) or (x < n - 1 and garden[x + 1][y] != v):
            fs.add((x + 1, y))
            # fs.add((x + 0.5, y))
        # check left + boundary
        if (y == 0) or (y > 0 and garden[x][y - 1] != v):
            fs.add((x, y - 1))
            # fs.add((x, y - 0.5))
        # check right + boundary
        if (y == m - 1) or (y < m - 1 and garden[x][y + 1] != v):
            fs.add((x, y + 1))
            # fs.add((x, y + 0.5))
        return fs

    def make_plot(x, y, p, v):
        if garden[x][y] != v:
            return
        # check top
        if x > 0 and garden[x - 1][y] == v and (x - 1, y) not in p:
            p.add((x - 1, y))
            make_plot(x - 1, y, p, v)
        # check bottom
        if x < n - 1 and garden[x + 1][y] == v and (x + 1, y) not in p:
            p.add((x + 1, y))
            make_plot(x + 1, y, p, v)
        # check left
        if y > 0 and garden[x][y - 1] == v and (x, y - 1) not in p:
            p.add((x, y - 1))
            make_plot(x, y - 1, p, v)
        # check right
        if y < m - 1 and garden[x][y + 1] == v and (x, y + 1) not in p:
            p.add((x, y + 1))
            make_plot(x, y + 1, p, v)

    visited = set()
    plots = []
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                # visit the current field
                visited.add((i, j))
                plot = set()
                plot.add((i, j))
                # construct plot
                make_plot(i, j, plot, garden[i][j])
                # visit the entire plot
                visited = visited.union(plot)
                # add the plot
                plots.append(plot)
    print(len(plots))
    result = 0
    for plot in plots:
        a = 0
        fields = set()
        for el in plot:
            f_perimeter = perimeter2(el[0], el[1])
            fields = fields.union(f_perimeter)
            a += 1
        # print("f", fields)
        xs = len(set([x[0] for x in fields]))
        ys = len(set([x[1] for x in fields]))
        p = xs + ys

        # xs = set([x[0] for x in fields])
        # ys = set([x[1] for x in fields])
        # p = len(xs.union(ys))
        # p = len(fields)

        result += (a * p)
        print(plot)
        print(a, p, "price", a * p)
    print(result)

p2()
