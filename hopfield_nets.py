def E(x0, x1, x2):
    e1 = x0 * x1 * 2 # the weights are 2, 1, and -1
    e2 = x1 * x2
    e3 = -x0 * x2
    return -(e1 + e2 + e3)

def print_all_energies():
    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                print(f"Nodes: {i}, {j}, {k} \nEnergy: {E(i, j, k)}\n")

def get_minimum_energy_values():
    curr_min = E(0, 0, 0)
    curr_values = [0, 0, 0]

    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                curr_energy = E(i, j, k)
                if curr_energy < curr_min:
                    curr_min = curr_energy
                    curr_values = [i, j, k]
    return (curr_values, curr_min)

if __name__ == "__main__":
    print_all_energies()
    print(get_minimum_energy_values())
