n, k = [int(i) for i in input().strip().split(' ')]
allSets = []
for i in range(n):
    allSets.append(set([int(i) for i in input().strip().split(" ")]))

intersectionSet = allSets[0]
for i in range(1, n):
    intersectionSet = intersectionSet & allSets[i]
print(" ".join(map(str, sorted(list(intersectionSet)))))
