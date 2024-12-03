def problem_1():
    def power(x, n):
        if n == 0:
            return 1
        return x * power(x, n - 1)
    print(power(2, 4))

def problem_2():
    def sum_digits(x):
        if len(str(x)) == 1:
            return int(x)
        return int(str(x)[0]) + sum_digits(str(x)[1:])
    print(sum_digits(248))

def problem_3(L, split):
    final, sublist = [], []
    for element in L:
        if element not in split:
            sublist.append(element)
        else:
            final.append(sublist.copy())
            sublist.clear()
    if len(sublist) != 0:
        final.append(sublist.copy())
    return final

if __name__ == "__main__":
    problem_1()
    problem_2()
    print(problem_3([1, 2, 6, 4, 5, 3, 7], [3, 6]))
