from collections import defaultdict
import itertools
from operator import itemgetter

graph = defaultdict(list)
nodeLevels = { 1 : 1, }
n = int(input())
for i in range(n - 1):
    u, v = [int(i) for i in input().strip().split(' ')]
    if u in nodeLevels.keys():
        nodeLevels[v] = nodeLevels[u] + 1
    else:
        # check if we already have level of v
        if v in nodeLevels.keys():
            nodeLevels[u] = nodeLevels[v] - 1
        else:
            # will have to resolve after the entire graph is built
            pass
        pass
    graph[u].append(v)

for level, group in itertools.groupby(\
    sorted(nodeLevels.items(), key=lambda x: x[1]),\
    lambda x: x[1]):
    if level % 2 == 1:
        print(" ".join(map(str, map(itemgetter(0), group))), end = " ")