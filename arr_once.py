from collections import *

n = int(input())
l = [int(i) for i in input().split(' ')]
l.sort()
d = defaultdict(int)
rep = []

for i in range(n):
    d[l[i]] += 1
    if d[l[i]] > 1:
        rep.append(l[i])

found = False
for i in range(len(l)):
    if l[i] not in rep:
        print(l[i], end = " ")
        found = True

if not found:
    print("no unique")
