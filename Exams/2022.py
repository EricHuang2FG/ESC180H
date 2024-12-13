def get_repeating_ints(L):
    unique = list(set(L))
    repeating_ints = []
    for num in unique:
        if L.count(num) > 1:
            repeating_ints.append(num)
    repeating_ints.sort()
    return repeating_ints

def my_median(L):
    for num in L:
        below, above = 0, 0
        for count_num in L:
            if count_num <= num:
                below += 1
            else:
                above += 1
        if below - 1 == above:
            return num

    # O(n^2)

def top_10_requests(requests: list) -> list:
    counting_dict = {}
    unique = list(set(requests))
    for request in unique:
        counting_dict[request] = requests.count(request)
    counting_dict = sorted(counting_dict.items(), key=lambda item: item[1], reverse=True)
    counting_dict = [pair[0] for pair in counting_dict][:10]
    counting_dict.sort()
    return counting_dict

def every_third(L):
    return [] if len(L) <= 2 else [L[2]] + every_third(L[3:])

# def build_chain(root, friends, chain, sub_chain, curr, i): # doesn't work. Time to brute force
#     if curr in sub_chain:
#         chain.append([root] + sub_chain)
#         return
#     next = friends[curr]
#     for friend in next:
#         if i == 0:
#             sub_chain = [curr]
#         if friend in sub_chain:
#             continue
#         sub_chain.append(friend)
#         build_chain(root, friends, chain, sub_chain, friend, 1)

def permutations(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list]
    
    all_perms = []
    for i, m in enumerate(list):
        remaining_list = list[:i] + list[i + 1:]
        for p in permutations(remaining_list):
            all_perms.append([m] + p)
    return all_perms

def subsets(list):
    results = [[]]
    for element in list:
        results += [subset + [element] for subset in results]
    return [i for i in results if len(i) > 1]

def is_chain_valid(friends: dict, chain: list):
    for i in range(len(chain) - 1):
        if chain[i + 1] not in friends[chain[i]]:
            return False
    return True

def longest_friendship_chain(friends: dict):
    friends_concact = list(friends.keys())

    # now we find every single possible path by brute force
    longest_chain_count = 0
    for possible_set in subsets(friends_concact):
        all_perms = permutations(possible_set)
        for chain in all_perms:
            if is_chain_valid(friends, chain):
                longest_chain_count = max(len(chain), longest_chain_count)
    return longest_chain_count

print(longest_friendship_chain({"Carl Gauss": ["Isaac Newton", "Gottfried Leibniz", "Charles Babbage"],
"Gottfried Leibniz": ["Carl Gauss"],
"Isaac Newton": ["Carl Gauss", "Charles Babbage"],
"Ada Lovelace": ["Charles Babbage", "Michael Faraday"],
"Charles Babbage": ["Isaac Newton", "Carl Gauss", "Ada Lovelace"],
"Michael Faraday": ["Ada Lovelace"]}))
