n = int(input())
nStr = str(n)
nRev = nStr[-1 : : -1]
if nStr == nRev:
    print("yes")
else:
    print("no")
