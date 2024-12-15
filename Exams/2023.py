import time

def print_gifts(names, gifts):
    for i in range(len(names)):
        print(f"{names[i]} will receive: {gifts[i]}")

def is_entry_in_matrix(e, M):
    for row in M:
        if e in row:
            return True
    return False

def has_three_white_in_a_row(L):
    i = 0
    while i < len(L):
        if L[i] == "w":
            count = 1
            while i < len(L):
                i += 1
                if i >= len(L):
                    break
                if L[i] == "w":
                    count += 1
                else:
                    break
            if count == 3:
                return True
        i += 1
    return False

print(has_three_white_in_a_row(["w", "w", "w", "w", "w", "w"]))

def merge_dict(A, B):
    merged_dict = {}
    for key, value in B.items():
        merged_dict[key] = value
    for key, value in A.items():
        if key in merged_dict:
            merged_dict[key] = [value, merged_dict[key]]
        else:
            merged_dict[key] = value

    return merged_dict

def remove_duplicate_words(sentence):
    words = sentence.split(" ")
    new_sentence = []
    for word in words:
        if word not in new_sentence:
            new_sentence.append(word)
    return " ".join(new_sentence)

def log(b, n):
    count = 0
    while True:
        n /= b
        if n <= 1:
            break
        count += 1
    return count

def estimate_complexity(f):
    # assume each call takes 0.0001 seconds for one loop execution
    input_size = 1000000
    start = time.time()
    f(input_size)
    end = time.time()
    execution_time = end - start
    num_calls = execution_time / 0.0001
    if input_size - 1000 <= num_calls <= input_size + 1000:
        return "O(n)"
    if (input_size ** 2) - 1000 <= num_calls <= (input_size ** 2) + 1000:
        return "O(n^2)"
    return "O(nlog n)"

def skip(list, count=0):
    if len(list) == 0:
        return []
    if count == 1:
        if list[0] % 2 == 0: # even
            return skip(list[1:], 0)
        return [list[0]] + skip(list[1:], count)
    else:
        if list[0] % 2 == 0: # even
            return [list[0]] + skip(list[1:], count + 1)
        return [list[0]] + skip(list[1:], count)

L = [[[1, 2], 3], [4]]
LI = []
for sublist in L:
    LI.append(sublist[:])
L[0][0][0] = 5
L[0][1] = 5
L[1][0] = 5
print(L)
print(LI)