n = int(input())
a = sorted([int(i) for i in input().strip().split(' ')])

leftIdx = 0
rightIdx = len(a) - 1

minSum = a[leftIdx] + a[rightIdx]
while leftIdx < rightIdx:
    thisSum = a[leftIdx] + a[rightIdx]
    if abs(thisSum) < minSum:
        minSum = abs(thisSum)
    
    if thisSum == 0:
        break
    elif thisSum > 0:
        rightIdx -= 1
    else:
        leftIdx += 1

print(minSum)

# Sample
# 5
# -1 2 3 1 0
