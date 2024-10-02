import math

def problem_1():
    tally = 0
    for i in range(1001):
        tally += ((-1) ** i) / (2 * i + 1)
    print(tally * 4)

def problem_2():
    i, tally = 0, 0
    while i < 1001:
        tally += ((-1) ** i) / (2 * i + 1)
        i += 1
    print(tally * 4)

def problem_3_a(n, m):
    def gcd(n, m):
        greatest = 0
        for i in range(1, min(n, m) + 1):
            if n % i == 0 and m % i == 0: 
                greatest = i
        return greatest
    print(gcd(n, m))

def problem_3_b(n, m):
    def gcd(n, m):
        p = min(n, m)
        while p > 0:
            if m % p == 0 and n % p == 0:
                return p
            p -= 1
    print(gcd(n, m))

def problem_4(n, m):
    def simplify_fraction(n, m):
        if m == 0:
            return print("Can't divide by 0!")
        d = math.gcd(n, m)
        numerator = n // d
        denominator = m // d
        if numerator == 0:
            print(0)
        elif denominator == 1:
            print(numerator)
        else:
            print(f"{numerator} / {denominator}")
    simplify_fraction(n, m)

def problem_5():
    all_names = ""
    while True:
        name = input("Enter a name: ")
        if name == "END":
            break
        all_names += f"{name}, "
    all_names = all_names[:-2]
    print(f"The names are: {all_names}")

def problem_6(n):
    tally, i = 0, 0
    while True:
        tally += ((-1) ** i) / (2 * i + 1)
        i += 1
        approximation = 4 * tally
        # round(x * (10 ** n)) gives n + 1 sig figs
        if round(approximation * (10 ** (n - 1))) == round(math.pi * (10 ** (n - 1))):
            return (i, approximation)

def problem_7_a(y, m, d):
    odd_months = [1, 3, 5, 7, 8, 10, 12]
    d += 1
    if (m in odd_months and d > 31) or (m not in odd_months and d > 30 and m != 2) or (m == 2 and y % 400 == 0 and d > 29) or (m == 2 and y % 400 != 0 and d > 28):
        m += 1
        d = 1
    if m > 12:
        y += 1
        m = 1
    return (y, m, d)

def problem_7_b(fY, fM, fD, tY, tM, tD):
    count = 0
    y, m, d = tY, tM, tD
    while True:
        if y == fY and m == fM and d == fD:
            break
        date = problem_7_a(y, m, d)
        print(date)
        y, m, d = date
        count += 1
    print(f"Number of days between: {count}")

def problem_8(n, m): # Euclidean Algorithm!
    small, big = min(n, m), max(n, m)
    r = big % small
    if r == 0:
        return small
    return problem_8(small, r)

if __name__ == "__main__":
    print(problem_8(33, 27))