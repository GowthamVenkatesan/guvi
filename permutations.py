import itertools

s = input().strip()
for thisPerm in itertools.permutations(s):
    print(''.join(thisPerm))
