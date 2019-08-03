n = int(input())
a = [int(i) for i in input().strip().split(" ")]
leftMax = a[0] - 1
rightMax = max(a[1:])

stars = []
superstars = []
for i in range(len(a)):
    if a[i] > rightMax:
        stars.append(a[i])
        if a[i] > leftMax:
            superstars.append(a[i])
        leftMax = a[i]
    if i == (len(a) - 2):
        rightMax = 0
    elif i == (len(a) - 1):
        # after this we will break
        pass
    else:
        rightMax = max(a[i+2:])
print(' '.join(map(str, stars)))
print(' '.join(map(str,superstars)))

# 4 2 1 7 2 1
