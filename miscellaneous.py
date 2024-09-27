# miscellaneous stuff go here!
from random import random

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

def main():
    approximate_pi(1000000)

if __name__ == "__main__":
    main()
    