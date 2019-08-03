from collections import Counter

n, k = [int(i) for i in input().strip().split()] 
a = [int(i) for i in input().strip().split()]
counter = Counter(a)

for e1 in counter.keys():
    if (k - e1) in counter.keys():
        if (k - e1) == e1:
            if counter[e1] == 2:
                print("YES")
                exit(0)
            else:
                pass
        else:
            print("YES")
            exit(0)
print("NO")
