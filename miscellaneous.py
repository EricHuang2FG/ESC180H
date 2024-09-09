# miscellaneous stuff go here!

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

def main():
    quadratic_solver(1, 2, -7)

if __name__ == "__main__":
    main()