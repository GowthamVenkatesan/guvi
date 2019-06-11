from collections import *

n = int(input())
l = [int(i) for i in input().split(' ')]
d = defaultdict(int)
rep = []

for i in range(n):
    d[l[i]] += 1
    if d[l[i]] == 2:
        rep.append(l[i])

rep.sort()
if len(rep) == 0:
    print("unique")
else:
    for i in range(len(rep)):
        print(rep[i], end=" ")
