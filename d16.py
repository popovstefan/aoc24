import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd16.txt"))

import sys
sys.setrecursionlimit(2500)


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


def p1_1(g, s, e, path=[]):
    path = path + [s]
    if s == e:
        return [path]
    if s not in g:
        return []
    paths = []
    for n in g[s]:
        if n not in path:
            nps = p1_1(g, n, e, path)
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
        # print("x1", x1, "y1", y1)
        # print("x2", x2, "y2", y2)
        # print(dr, ndr, nchanges)
        dr = ndr
        fpos = npos
    cost = 1000 * nchanges + len(path) - 1
    m_cost = min(cost, m_cost)
print("min cost", m_cost)
