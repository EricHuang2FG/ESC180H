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

if __name__ == "__main__":
    exec_stringified_code()
    