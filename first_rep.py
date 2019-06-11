from collections import *

n = int(input())
l = [int(i) for i in input().split(' ')]
d = defaultdict(int)

found = False
for i in range(n):
    d[l[i]] += 1
    if d[l[i]] == 2:
        print(l[i])
        found = True

if not found:
    print("unique")