n = int(input())
strings = []
for i in range(n):
    strings.append(input().strip())

smallestStr = strings[0]
smallestLength = len(smallestStr)

for i in range(n):
    # print("comparing: ", smallestStr, " and, " , strings[i])
    idx = strings[i].find(smallestStr)
    # print('idx: ', idx)
    if idx == -1:
        # find the common thing b/w the 2 strings
        commLen = 0
        while strings[i][0: commLen]  == smallestStr[0: commLen]:
            # print('commLen: ', commLen, ", strings:", strings[i][0:commLen], ", smallestStr:", smallestStr[0:commLen])
            if commLen >= smallestLength:
                break
            commLen += 1
        commLen -= 1
        smallestStr = smallestStr[0: commLen]
        smallestLength = commLen

print(smallestStr)
