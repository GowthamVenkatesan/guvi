s = input()
res = " ".join([i[::-1] for i in s.strip().split(' ')])
print(res)
