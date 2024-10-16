def problem_1():
    L = [
        ["CIV", 92],
        ["180", 98],
        ["103", 99],
        ["194", 95]
    ]
    for sub in L:
        for element in sub:
            if element == 99:
                print(element)
                break
        else:
            continue
        break        

def problem_2():
    L = [
        ["CIV", 92],
        ["180", 98],
        ["103", 99],
        ["194", 95]
    ]
    result = []
    for sub in L:
        result.append(sub[1])
    return result

def problem_3():
    L = [
        ["CIV", 92],
        ["180", 98],
        ["103", 99],
        ["194", 95]
    ]
    def lookup(L, num):
        for sub in L:
            if sub[1] == num:
                return sub[0]
        return None
    print(lookup(L, 99))

def problem_4():
    # a) since the energy is the sum of the negative of the products of the two nodes and the weight,
    # then if the product of the nodes is greater than zero, if will decrease the total energy
    w01, w02, w12 = 2, -1, 1
    def E(x0, x1, x2, w01, w02, w12):
        term1 = x0 * x1 * w01
        term2 = x1 * x2 * w12
        term3 = x0 * x2 * w02
        return -(term1 + term2 + term3)
    def print_all_energies(w01, w02, w12):
        for x0 in [-1, 1]:
            for x1 in [-1, 1]:
                for x2 in [-1, 1]:
                    print(f"x: ({x0}, {x1}, {x2}), E: {E(x0, x1, x2, w01, w02, w12)}")

    # part b)
    print_all_energies(w01, w02, w12)
    print()
    x0, x1, x2 = -1, 1, 1
    def adjust_weight(x0, x1, x2, w01, w02, w12):
        if x0 * x1 > 0:
            w01 += 0.1
        else:
            w01 -= 0.1
        if x0 * x2 > 0:
            w02 += 0.1
        else:
            w02 -= 0.1
        if x1 * x2 > 0:
            w12 += 0.1
        else:
            w12 -= 0.1
        return (w01, w02, w12)
    w01, w02, w12 = adjust_weight(x0, x1, x2, w01, w02, w12)
    print_all_energies(w01, w02, w12)
    print()

    # part c) and d)
    x0, x1, x2 = -1, 1, 1
    w01, w02, w12 = 2, -1, 1
    for i in range(5):
        w01, w02, w12 = adjust_weight(x0, x1, x2, w01, w02, w12)
        print_all_energies(w01, w02, w12)
        print("---------------------")
    
    # part e)
    x0, x1, x2 = -1, 1, 1
    w01, w02, w12 = 2, -1, 1
    def weight_after_memory_stored(x0, x1, x2, w01, w02, w12):
        while True:
            all_energies = {}
            w01, w02, w12 = adjust_weight(x0, x1, x2, w01, w02, w12)
            for i in [-1, 1]:
                for j in [-1, 1]:
                    for k in [-1, 1]:
                        all_energies[(i, j, k)] = E(i, j, k, w01, w02, w12)
            min_energy = min(all_energies.values())
            for key, value in all_energies.items():
                if value == min_energy and key == (x0, x1, x2):
                    return [w01, w02, w12]
    print(weight_after_memory_stored(x0, x1, x2, w01, w02, w12))

    # part f)
    x0, x1, x2 = 1, -1, 1
    w01, w02, w12 = 2, -1, 1
    w01, w02, w12 = weight_after_memory_stored(x0, x1, x2, w01, w02, w12)
    print((w01, w02, w12))

if __name__ == "__main__":
    problem_1()
    print(problem_2())
    problem_3()
    problem_4()
