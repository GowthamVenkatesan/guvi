n = int(input())
l = [int(i) for i in input().split(' ')]
l.sort(reverse=True)
res = 0
for i in range(n):
    res *= 10
    res += l[i]
print(res)
