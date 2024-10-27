def zeros(x):
    count = 0
    while True:
        if x >= 0.1 and x < 1:
            return count
        x *= 10.0
        count += 1

def kids_who_favour_popular(faves):
    candies = list(faves.values())
    unique = list(set(candies))
    most_popular, max_c = "", 0
    for candy in unique:
        if candies.count(candy) > max_c:
            most_popular = candy
            max_c = candies.count(candy)
    
    all_kids = []
    for key, value in faves.items():
        if value == most_popular:
            all_kids.append(key)
    return all_kids

def E(x1, x2, x3, x4):
    return -(x1 * x2 + x2 * x3 + x3 * x4 + x1 * x4)

def minimize_energy(epsilon):
    tally = {}
    for i in [1, -1]:
        for j in [1, -1]:
            for k in [1, -1]:
                for l in [1, -1]:
                    comb = (i, j, k, l)
                    energy = E(i, j, k, l)
                    if comb not in tally:
                        tally[comb] = energy
    min_energy = min(tally.values())
    within_epsilon = []
    for comb, energy in tally.items():
        if energy >= min_energy and energy <= min_energy + epsilon:
            within_epsilon.append([i for i in comb])
    return within_epsilon

if __name__ == "__main__":
    print(zeros(0.000001))
    print(kids_who_favour_popular({"Charlie": "Mars", "Eric": "Snickers", "Hello": "Mars"}))
    print(minimize_energy(0.1))
