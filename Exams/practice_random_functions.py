def selection_sort(L):
    for i in range(len(L) - 1):
        curr_max, curr_max_index = L[0], 0
        for j in range(len(L) - i):
            if L[j] > curr_max:
                curr_max = L[j]
                curr_max_index = j
        L[len(L) - i - 1], L[curr_max_index] = L[curr_max_index], L[len(L) - i - 1]
    return L

def permutations(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list]
    
    all_perms = []
    for i in range(len(list)):
        m = list[i]
        remaining_list = list[:i] + list[i + 1:]
        for p in permutations(remaining_list):
            all_perms.append(p + [m])
    return all_perms

def f(d):
    d1 = {}
    for k in d:
        d1[k] = d[k]
    return d1
d = {1:[[1, 2]], 0:[[3, 4]]}
d1 = f(d)
d1[0][0][0] = 5
print(d[0])
