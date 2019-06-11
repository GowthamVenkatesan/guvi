n = int(input())
l = [int(i) for i in input().strip().split(' ')]
partialSums = []
for i in range(n):
    thisSum = 0
    for j in range(i):
        thisSum += l[j]
    partialSums.append(thisSum)
print(sum(partialSums))
