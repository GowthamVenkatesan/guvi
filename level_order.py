graph = {}
n = int(input())
for i in range(n - 1):
    u, v = [int(i) for i in input().strip().split(' ')]
    graph[u] = v

thisRoot = 1
print(thisRoot, end = " ")
try:
    while True:
        thisRoot = graph[thisRoot]
        thisRoot = graph[thisRoot]
        print(thisRoot, end = " ")
except KeyError:
    # we're done
    pass