m, n = [int(i) for i in input().strip().split(' ')]
a = set([int(i) for i in input().strip().split(' ')])
b = set([int(i) for i in input().strip().split(' ')])

if b.issubset(a):
    print("YES")
else:
    print("NO")

# sample
# 7 6
# 1 2 3 4 5 6 7
# 3 4 5 6 7 1
