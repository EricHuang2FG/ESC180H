# miscellaneous stuff go here!

from random import random
import time
import matplotlib.pyplot as plt

def quadratic_solver(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        r1 = round((-b + disc ** 0.5) / (2 * a), 2)
        r2 = round((-b - disc ** 0.5) / (2 * a), 2)
        print(f"The roots are: {r1}, {r2}")
    elif disc == 0:
        r1 = round((-b + disc ** 0.5) / (2 * a), 2)
        print(f"The root is {r1}")
    else:
        print("No real roots :(")

def has_roots(a, b, c):
    return b ** 2 - 4 * a * c >= 0

def multiply(a, b):
    total = 0
    for i in range(b):
        total += a
    return total

def inside_unit_circle(x, y):
    return x ** 2 + y ** 2 <= 1

def approximate_pi(N):
    # generate N random points
    # keep track of M, which is the number of points inside the unit quarter-circle
    # computer 4 * N / M
    M = 0
    for i in range(N):
        x, y = random(), random()
        if inside_unit_circle(x, y):
            M += 1
    print(4 * M / N)

def all_combinations():
    alphabet = ['a', 'b', 'c', 'd']
    for l1 in alphabet:
        for l2 in alphabet:
            for l3 in alphabet:
                for l4 in alphabet:
                    for l5 in alphabet:
                        print(l1 + l2 + l3 + l4 + l5)

def exec_stringified_code():
    code = "print(123); print(132); print(123212321)"
    exec(code)

    print(eval("123 + 456"))
    exec("123 + 456")

    code = "alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']\n"

    for i in range(1, 20):
        line = f'{4 * (i - 1) * " "}for char{i} in alphabet:\n'
        code += line
    line = " " * (i + 1) * 4
    line += "print("
    for i in range(1, 20):
        line += f"char{i} + "
    line += "'')\n"
    code += line
    
    print(code)
    exec(code)

def some_memory_addresses():
    # at first, the memory addresses alternate because if nothing points to it, it gets deleted from memory
    # -5 to 256 are pre-stored so you see different memory addresses
    for i in range(-10, 260):
        print(i, id(i))

def compound_objects_memory():
    L = [[1, 2], [3, 4]]
    L1 = [L[0], L[1]]  # currently L and L1 are equal
    # L and L1 are separate lists, not aliases
    # BUT, L1[0] is an alias of L[0], and L1[1] is an alias of L[1], and vice versa

    # id(L[0]) == id(L1[0]) because those are aliases

    L[0][0] = 5 # this will change both L and L1


# N possible gueses
# Ask a yes/no question
# N/2 possible guesses
# Ask a yes/no question
# N/4 possible guesses
# ...
# until it reaches 1
# So there are log_2(N) questions to get from N to 1

def binary_search(L, e):
    low = 0
    high = len(L) - 1
    while low < high:
        mid = (low + high) // 2
        if L[mid] == e:
            return mid
        elif L[mid] < e:
            low = mid + 1
        else:
            high = mid - 1
    if L[low] == e:
        return low
    if L[high] == e:
        return high
    return None

    # this is O(log(n))

def runtime_complexities():
    def find_e(L, e):
        for i in range(len(L)):
            if L[i] == e:
                return i
        return -1
    # for find_e(), the runtime is porportional to n, where n = len(L)
    # for binary search, the runtime is porportional to log2(n)

    # let g(n) be the runtime for input of size n
    # and f(n) is the complexity

    # the worst-case asymptotic runtime complexity of find_e is O(n)
    # g(n) is O(f(n)) if limit of sup as n approaches infinity of g(n) / f(n) < c
    # informally, g grows at most as fast as f

    # limit of sup h(n) as n approaches infinity is the limit as n approaches infinity if the least upper bound of h(k)

def linear_search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return i

def quaratic_search_fake(L, e):
    for _ in range(len(L) ** 2):
        pass

def timeit(f, arg1, arg2):
    n_runs = 1000
    start_t = time.time()
    for _ in range(n_runs):
        f(arg1, arg2)
    end_t = time.time()
    return (end_t - start_t) / n_runs

def check_runtimes():
    lengths = [0, 1, 10, 100]
    runtimes = []
    runtimes_sq = []
    for length in lengths:
        runtimes.append(timeit(linear_search, [0] * length, 1))
        runtimes_sq.append(timeit(quaratic_search_fake, [0] * length, 1))
    plt.plot(runtimes, lengths)
    plt.plot(runtimes_sq, lengths)
    plt.show()

def complexities():
    def f(m, n):
        for _ in range(n):
            for _ in range(m):
                pass
    # complexity of f is m * n, so O(m * n)

    def g(n):
        for _ in range(n):
            for _ in range(n // 2):
                pass
    # complexity of g is n^2 / 2, so O(n^2)

    # Project 3 hint:
    # for sentence in sentences:
    #     for word in sentence:
    #         for word2 in sentence:
    #             pass # update d[word][word2]
    # O(m * k ^ 2), where k is the longest possible sentence, and m is the number of sentences

def sorting_algorithms():
    def selection_sort(L):
        # pick the largest element, put it in position n - 1
        # pick the next largest, put it in position n - 2
        # pick the next largest, put it in position n - 3
        n = len(L)
        for i in range(n - 1):
            curr_max_index, curr_max = 0, L[0]
            for j in range(len(L) - i):
                if L[j] > curr_max:
                    curr_max_index, curr_max_index = L[j], j
            L[curr_max_index], L[len(L) - i - 1] = L[len(L) - i - 1], L[curr_max_index]
        return L
        # O(n^2)
    
    def counting_sort(L):
        # construct a list of counts
        # counts[e] is the number of times e appears
        # Reconstruct the sorted version of the list using the counts
        # [i] * counts[i] for every i
        counts = [0] * (max(L) + 1)
        for e in L:
            counts[e] += 1
        res = []
        for i in range(len(counts)):
            res.extend([i] * counts[i])
        return res
    print(selection_sort([5, 10, 12, 3, 2, 1, 100]))

# now let's do some race to 21
# player is guaranteed to win assuming they follow perfect strategy
# Player 1 is at 0 initially
# I know that if n is 18, player 1 loses
#                     19, player 1 wins
#                     20, player 1 wins
#                     21, player 1 loses

# Strategy:
# Write out base cases
# Express the answer to what the output of f is in terms of calls to f itself
def is_win(n):
    if n == 21:
        return False
    if n == 20:
        return True
    if n == 19:
        return True

    moves = [1, 2]
    for move in moves:
        if not is_win(n + move):
            return True
    return False

def print_list(L):
    if len(L) == 0:
        return
    return print(L[0]) + print_list(L[1:])

def print_list_reverse(L):
    if len(L) == 0:
        return
    return print_list_reverse(L[1:]) + print(L[0])

def sum_list(L):
    if len(L) == 0:
        return 0
    if len(L) == 1:
        return L[0]
    return L[0] + sum_list(L[1:])

def sum_list_half_method(L):
    '''Return the sum of the list of ints L'''
    if len(L) == 0:
        return 0
    
    if len(L) == 1:
        return L[0]  #the sum of the list is L[0] if L[0] is the only element
    
    mid = len(L)//2 #(the index of the approximate midpoint of the list)
    return sum_list_half_method(L[:mid]) + sum_list_half_method(L[mid:])

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

# Runtime complexity of power?
# You go from 0 to n, making n + 1 calls. Each call takes the same amount of time
# Suppose that time is t1, then the total time is t1 * (n + 1)
# This means the runtime complexity is O(n)

def power_fast(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    half_n = n // 2
    half_power = power_fast(x, half_n)
    almost_full_power = half_power * half_power
    if n % 2 == 0:
        return almost_full_power
    return almost_full_power * x
    # O(log n)

    # (2^(n + 1) - 1) / (2 - 1) ~= 2^(n + 1) = 2 ^ 2 ^ n
    # KNOW THE GEOMETRIC SERIES FORMULA

    # for recursively dividing a list:
    # 2^0 + 2^1 + 2^2 + ... + 2^(log2(n))
    # so summing with a geometric series, we get O(n)

def merge(L1, L2):
    res = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            res.append(L1[i])
            i += 1
        else:
            res.append(L2[j])
            j += 1
    
    # one of those is going to be empty
    res.extend(L1[i:])
    res.extend(L2[j:])
    return res

def merge_sort(L):
    if len(L) <= 1:
        return L.copy()
    mid = len(L) // 2
    return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))

if __name__ == "__main__":
    print(sum_list([1, 2, 3]))
