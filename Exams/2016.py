def is_fib(L):
    if len(L) == 0:
        return True
    if L == [1] or L == [1, 1]:
        return True
    if len(L) <= 2:
        return False
    if L[-1] != L[-3] + L[-2]:
        return False
    return is_fib(L[:len(L) - 1])

def max_rec(L):
    if len(L) == 0:
        return
    if len(L) == 1:
        return L[0]
    if len(L) == 2:
        return L[0] if L[0] > L[1] else L[1]
    if L[0] > L[1]:
        return max_rec([L[0]] + L[2:])
    return max_rec(L[1:])

def sorted_timestamps(timestamps):
    positions = [0] * 60 * 24
    for time in timestamps:
        hour, minute = time
        positions[hour * 60 + minute] += 1
    
    sorted_timestamps = []
    for i in range(60 * 24):
        if positions[i] != 0:
            sorted_timestamps.extend([(i // 60, i % 60)] * positions[i])
    return sorted_timestamps

def permutations(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list]

    all_perms = []
    for i in range(list):
        m = list[i]
        remaining_list = list[:i] + list[i + 1:]
        for p in permutations(remaining_list):
            all_perms.append([m] + p)
    return all_perms

def subsets(list):
    results = [[]]
    for element in list:
        results += [subset + [element] for subset in results]
    return results

def is_clique(subset, mapping):
    if len(subset) == 0:
        return False
    for i, a in enumerate(subset):
        for j in range(i + 1, len(subset)):
            if subset[j] not in mapping[a]:
                return False
    return True

def max_clique(friends):
    largest_clique = []
    for person, friend_list in friends.items():
        all_subsets = subsets([person] + friend_list)
        for subset in all_subsets:
            if is_clique(subset, friends):
                largest_clique = subset if len(subset) > len(largest_clique) else largest_clique
    return largest_clique

print(max_clique( {"Carl Gauss": ["Isaac Newton", "Gottfried Leibniz", "Charles Babbage"],
"Gottfried Leibniz": ["Carl Gauss"],
"Isaac Newton": ["Carl Gauss", "Charles Babbage"],
"Ada Lovelace": ["Charles Babbage", "Michael Faraday"],
"Charles Babbage": ["Isaac Newton", "Carl Gauss", "Ada Lovelace"],
"Michael Faraday": ["Ada Lovelace"] }))
