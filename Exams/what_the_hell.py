def mystery_helper(L, k):
    p = max(L[0], L[-1])
    L1 = []
    L2 = []
    for e in L:
        if e < p:
            L1.append(e)
        else:
            L2.append(e)
    if len(L1) > k:
        return mystery_helper(L1, k)
    elif len(L1) < k:
        return mystery_helper(L2, k-len(L1))
    else:
        return p

help = [1, 2, 3, 4]
# print(mystery_helper(help, 3))

def f(d):
    d1 = {}
    for k in d:
        d1[k] = d[k]
    return d1
d = {1:[[1, 2]], 0:[[3, 4]]}
d1 = f(d)
d1[0][0][0] = 5
print(d[0])