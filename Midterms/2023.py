def print_halloween(month, day):
    if month == "oct" and day == 31:
        print("Happy Haloween")
    else:
        print("Not Haloween")

def sum_even_squares(L):
    total = 0
    for num in L:
        if num % 2 == 0:
            total += num ** 2
    return total

def is_sorted(L):
    if list(set(L)) != L:
        return False
    dummy = L.copy()
    dummy.sort()
    if L not in [dummy, dummy[::-1]]:
        return False
    return True

def print_trick_or_treat_for(name):
    if name in ["cluett", "stangeby"]:
        print("trick")
    elif name == "davis":
        print("treat")
    else:
        print("no candy for you")

def count_occurrences(n, target):
    return len([i for i in n if i == target])

def most_frequent_fave(faves):
    unique = list(set(faves))
    max_item, count = "", 0
    for val in unique:
        if faves.count(val) > count:
            count = faves.count(val)
            max_item = val
    return max_item

inputs = []
done = False

def find_next_prime(curr):
    i = curr + 1
    while True:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            return i
        i += 1

def check_next_prime(n):
    global done, inputs
    if done:
        print("Game is over")
        return
    if len(inputs) == 0:
        if n == 2:
            print("Correct")
            inputs.append(n)
        else:
            print("Incorrect, game over")
            done = True
    elif n == find_next_prime(inputs[-1]):
        print("Correct")
        inputs.append(n)
    else:
        print("Incorrect, game over")
        done = True

def is_almost_symmetric(M):
    def is_symmetric(M):
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[j][i] != M[i][j]:
                    return False
        return True

    for i in range(len(M)):
        for j in range(len(M[0])):
            for k in range(len(M)):
                for l in range(len(M[0])):
                    M[i][j], M[k][l] = M[k][l], M[i][j]
                    if is_symmetric(M):
                        return True
                    M[i][j], M[k][l] = M[k][l], M[i][j]
    return False

if __name__ == "__main__":
    print(is_almost_symmetric([[1, 2, 4], [2, 5, 9], [4, 3, 3]]))
    check_next_prime(2)
    check_next_prime(3)
    check_next_prime(5)
    check_next_prime(7)
    check_next_prime(10)
    check_next_prime(123123123123123123)
    print(is_sorted([1, 2, 5, 4, 5]))
