import numpy as np

n, m = [int(i) for i in input().strip().split(" ")]
mat = []
for r in range(n):
    mat.append([int(i) for i in input().strip().split(" ")])

npMat = np.array(mat)
resMat = npMat.copy()
for r in range(n):
    # row check
    idxs = np.where(npMat[r,:] == 0)[0]
    for idx in idxs:
        # make col as zero
        resMat[:, idx] = 0
    if len(idxs > 0):
        resMat[r, :] = 0
for row in resMat.tolist():
    print(" ".join(map(str, row)))
