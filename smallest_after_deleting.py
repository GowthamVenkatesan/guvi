n, k = input().strip().split(' ')
k = int(k)

n = n[k: ]
if '0' in n:
    for i in range(1, 10):
        if i in n:
            print(i, end="")
            n.remove(str(i))
n = list(n)
n.sort()
for i in range(len(n)):
    print(n[i], end="")
