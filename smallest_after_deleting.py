n, k = input().strip().split(' ')
k = int(k)
n = list(n)
n.sort()

n = n[0: len(n)-k]
if '0' in n:
    for i in range(1, 10):
        if i in n:
            print(i, end="")
            n.remove(str(i))
for i in range(len(n)):
    print(n[i], end="")
