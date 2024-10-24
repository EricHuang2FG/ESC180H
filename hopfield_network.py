w01, w02, w12 = 2, -1, 1
x0, x1, x2 = -1, 1, 1

def E(x0, x1, x2):
    e1 = x0 * x1 * w01
    e2 = x1 * x2 * w12
    e3 = x0 * x2 * w02
    return -(e1 + e2 + e3)

def print_all_energies():
    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                print(f"Nodes: {i}, {j}, {k} \nEnergy: {E(i, j, k)}\n")

def adjust_weights():
    global w01, w02, w12
    if x0 * x1 > 0:
        w01 += 0.1
    else:
        w01 -= 0.1
    if x1 * x2 > 0:
        w12 += 0.1
    else:
        w12 -= 0.1
    if x0 * x2 > 0:
        w02 += 0.1
    else:
        w02 -= 0.1

def get_minimum_energy_values():
    min_energy, min_nodes = None, None
    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                curr_energy = E(i, j, k)
                if not min_energy or curr_energy < min_energy:
                    min_energy = curr_energy
                    min_nodes = (i, j, k)
    return (min_nodes, min_energy)

def store_in_memory():
    while True:
        adjust_weights()
        if (x0, x1, x2) == get_minimum_energy_values()[0]:
            print(f"Min energy nodes: {x0}, {x1}, {x2} \nEnergy: {E(x0, x1, x2)}\n")
            print_all_energies()
            return

if __name__ == "__main__":
    store_in_memory()
