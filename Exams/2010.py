def flatten(L):
    flattened = []
    def traverse(L):
        if not isinstance(L, list) or len(L) == 0:
            return
        if L[0] and not isinstance(L[0], list):
            flattened.append(L[0])
        else: traverse(L[0])
        traverse(L[1:])
    traverse(L)
    return flattened

def add_neighbours(L):
    new_list = []
    
    # handle edge cases
    if len(L) == 0:
        return []
    if len(L) == 1:
        return L
    for index, value in enumerate(L):
        if index == 0:
            new_list.append(value + L[index + 1])
        elif index == len(L) - 1:
            new_list.append(value + L[index - 1])
        else:
            new_list.append(value + L[index - 1] + L[index + 1])
    return new_list
