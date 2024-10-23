def halloween_reaction(thing):
    if thing in ["ghost", "monster", "midterm"]:
        return "NOO!"
    return "YAY!"

def print_mid_part(L):
    for index, value in enumerate(L):
        if index == 0 or index == len(L) - 1:
            continue
        print(value)

def h(L):
    L[0] = "fall"
    L[1] = "colours"

def odds_sum(L):
    L = [i for i in L if i % 2 != 0]
    return sum(L)

def while_loop():
    i = 5
    while i < 500:
        print(i)
        i += 3

def kids_who_like_candy(faves, kids):
    names = []
    for index, kid in enumerate(kids):
        if faves[index] == "candy":
            names.append(kid)
    return names

def cube_root(n):
    ans = 0
    for i in range(abs(n) + 1):
        if i * i * i == abs(n):
            ans = i
            break
    ans = -ans if n < 0 else ans
    return ans

count = 4
def halloween_surprise():
    global count
    if count > 1:
        count -= 1
        return count
    return "SURPRISE!"

def has_single_peak(L):
    is_dec = False
    if len(L) <= 2:
        return True
    for i in range(len(L) - 1):
        if is_dec and L[i + 1] > L[i]:
            return False
        if not is_dec and L[i + 1] < L[i]:
            is_dec = True
    return True

def max_arrivals_2hrs(arrivals):
    max_count, count = 0, 0
    for i, starting_time in enumerate(arrivals):
        count = 0
        for j in range(i, len(arrivals)):
            if arrivals[j] <= starting_time + 120:
                count += 1
            else:
                break
        if count > max_count:
            max_count = count
    return max(max_count, count)

if __name__ == "__main__":
    print(max_arrivals_2hrs([0, 30, 40, 150, 160, 170, 370]))
