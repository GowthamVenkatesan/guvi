string = list(input().strip())
stack = string.copy()

for i in range(len(string)):
    if stack.pop() != string[i]:
        print("NO")
        exit(0)

print("YES")
