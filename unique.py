from collections import Counter

n = int(input())
a = [int(i) for i in input().strip().split(' ')]

c = Counter(a)
if len(c) == n:
    print("unique")
else:
    repeated = []
    for k, v in c.items():
        if v > 1:
            repeated.append(v)
    print(sorted(repeated))

# Sample ip
# 7
# 1 2 3 2 3 4 3
