import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd5.txt"))

# parse input
page_rules = []
printing_queue = []

for line in puzzle_input:
    if line.strip() == "":
        continue
    elif "|" in line:
        parts = line.split("|")
        page_rules.append((int(parts[0].strip()), int(parts[1].strip())))
    else:
        parts = line.split(",")
        q = []
        for part in parts:
            q.append(int(part.strip()))
        printing_queue.append(q)

# print(printing_queue)

# make graph
graph = {}
for src, dst in page_rules:
    if not src in graph:
        graph[src] = {
            "before": [],
            "after": []
        }
    if not dst in graph:
        graph[dst] = {
            "before": [],
            "after": []
        }
    graph[src]["after"].append(dst)
    graph[dst]["before"].append(src)

print(graph)


def p1():
    def eval_rule(u, v):
        # v should be after u
        # u should be before v
        before_v = set(graph[v]["before"])
        after_u = set(graph[u]["after"])
        return v in after_u and u in before_v

    solution = 0
    for pq in printing_queue:
        result = True
        for inx in range(len(pq) - 1):
            result &= eval_rule(pq[inx], pq[inx + 1])
        if result:
            solution += pq[int(len(pq) / 2)]
    print(solution)

def p2():
    pass


p1()
