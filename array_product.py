from functools import reduce
n = int(input())
a = [int(i) for i in input().strip().split(' ')]
fullProd = reduce(lambda x, y: x * y, a)
for i in a:
    print(fullProd//i, end=" ")
