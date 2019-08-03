n, k = [int(i) for i in input().strip().split(' ')]
a = [int(i) for i in input().strip().split(' ')]
a = list(set(a))

print(sorted(a, reverse=True)[k-1])
