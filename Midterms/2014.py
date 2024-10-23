def permutation(val):
    if len(val) <= 1:
        return [val]
    
    perms = []
    for i in range(len(val)):
        pivot = val[i]
        sliced = val[:i] + val[i + 1:]
        for perm in permutation(sliced):
            perms.append(pivot + perm)
    return perms

def near_anagram(w1, w2):
    for perm in permutation(w1):
        count = 0
        for index, letter in enumerate(perm):
            if letter != w2[index]:
                count += 1
            if count > 1:
                break
        if count == 1:
            return True
    return False

def print_letter():
    L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for i in L:
        for j in L:
            for k in L:
                for l in L:
                    temp = i + j + k + l
                    if temp.count(i) <= 2 and temp.count(j) <= 2 and temp.count(k) <= 2 and temp.count(l) <= 2:
                        print(temp)

def flatten(list_of_lists):
    flattened = []
    for sub_list in list_of_lists:
        for element in sub_list:
            flattened.append(element)
    return flattened

if __name__ == "__main__":
    print_letter()
