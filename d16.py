import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd16.txt"))

import sys

sys.setrecursionlimit(5500)

grid = []

for i, line in enumerate(puzzle_input):
    grid.append([])
    for char in line:
        grid[i].append(char)

N = len(grid)
M = len(grid[0])
# print(grid)

graph = {}

spos = (0, 0)
epos = (0, 0)
for i in range(N):
    for j in range(M):
        if grid[i][j] != '#':
            if grid[i][j] == 'S':
                spos = (i, j)
            if grid[i][j] == 'E':
                epos = (i, j)
            pos = f"{i}-{j}"
            if pos not in graph:
                graph[f"{i}-{j}"] = []
            if i > 0 and grid[i - 1][j] != '#':
                graph[pos].append(f"{i - 1}-{j}")
            if i < N and grid[i + 1] != '#':
                graph[pos].append(f"{i + 1}-{j}")
            if j < M and grid[i][j + 1] != '#':
                graph[pos].append(f"{i}-{j + 1}")
            if j > 0 and grid[i][j - 1] != '#':
                graph[pos].append(f"{i}-{j - 1}")

default_mcs = 213716
mcs = default_mcs


def calc_cost(p):
    global mcs, default_mcs
    fpos = p[0]
    dr = '>'
    ndr = 'o'
    nchanges = 0
    for npos in p[1:]:
        fp = fpos.split("-")
        x1, y1 = int(fp[0]), int(fp[1])
        np = npos.split("-")
        x2, y2 = int(np[0]), int(np[1])
        if x1 + 1 == x2:
            ndr = 'v'
        if x1 - 1 == x2:
            ndr = '^'
        if y1 + 1 == y2:
            ndr = '>'
        if y1 - 1 == y2:
            ndr = '<'
        if dr != ndr:
            nchanges += 1
        if dr == '^' and ndr == 'v':
            nchanges += 1
        if ndr == '^' and dr == 'v':
            nchanges += 1
        if dr == '>' and ndr == '<':
            nchanges += 1
        if ndr == '>' and dr == '<':
            nchanges += 1
        dr = ndr
        fpos = npos
        c = 1000 * nchanges + len(p) - 1
        if mcs < default_mcs and c >= mcs:
            return c
    return 1000 * nchanges + len(p) - 1


def p1_1(g, s, e, path=[]):
    global mcs
    if s in path:
        yield []
        return
    path = path + [s]
    c = calc_cost(path)
    if mcs < default_mcs and c >= mcs:
        yield []
        return
    if s == e:
        if c < mcs:
            mcs = c
            print("mcs", mcs)
            yield [path]
            return
        yield []
        return
    if s not in g:
        yield []
        return
    paths = []
    for n in g[s]:
        if n not in path:
            c = calc_cost(path)
            if c > mcs:
                continue
            nps = [x for x in p1_1(g, n, e, path) if len(x) > 0]
            for np in nps:
                paths.append(np)
    return paths


all_paths = p1_1(graph, f"{spos[0]}-{spos[1]}", f"{epos[0]}-{epos[1]}", [])
# print(spos, epos)

m_cost = float("inf")
for path in all_paths:
    fpos = path[0]
    dr = '>'
    ndr = 'o'
    nchanges = 0
    cost = 0
    for npos in path[1:]:
        fp = fpos.split("-")
        x1, y1 = int(fp[0]), int(fp[1])
        np = npos.split("-")
        x2, y2 = int(np[0]), int(np[1])
        if x1 + 1 == x2:
            ndr = 'v'
        if x1 - 1 == x2:
            ndr = '^'
        if y1 + 1 == y2:
            ndr = '>'
        if y1 - 1 == y2:
            ndr = '<'
        if dr != ndr:
            nchanges += 1
            dir_chng = True
        if dr == '^' and ndr == 'v':
            nchanges += 1
        if ndr == '^' and dr == 'v':
            nchanges += 1
        if dr == '>' and ndr == '<':
            nchanges += 1
        if ndr == '>' and dr == '<':
            nchanges += 1
        dr = ndr
        fpos = npos
        cost = 1000 * nchanges + len(path) - 1
        if cost > m_cost:
            break
    m_cost = min(cost, m_cost)
print("min cost", m_cost)
