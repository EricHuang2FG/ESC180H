import math

# question 1
def get_perfect_squares(n):
    result = []
    for i in range(math.floor(math.sqrt(n)) + 1):
        result.append(pow(i, 2))
    return result

def prod(L):
    product = 1
    for val in L:
        product *= val
    return product

def duplicates(list0):
    for i in range(len(list0) - 1):
        if list0[i] == list0[i + 1]:
            return True
    return False

def prompt_order():
    count = 0
    in_str = ""
    while True:
        in_str = input("What is your order? (User input:)")
        if in_str.lower() == "pumpkin spice latte":
            print(count)
            break
        count += 1

def matrix_sum(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "ERROR"
    result = []
    for i, row in enumerate(A):
        result_row = []
        for j, value in enumerate(row):
            result_row.append(value + B[i][j])
        result.append(result_row)
    return result

def luckiest_kid(haul_dataset):
    tally = {}
    for people in haul_dataset.values():
        for person, candies in people.items():
            if person in tally:
                tally[person] += len(candies)
            else:
                tally[person] = len(candies)
    name, count = "", 0
    for key, value in tally.items():
        if value > count:
            count = value
            name = key
    return name

ptr = 0

def next_digit_pi():
    global ptr
    pi_str = str(math.pi).replace(".", "")[ptr]
    ptr += 1
    return pi_str

if __name__ == "__main__":
    print(get_perfect_squares(5))
    print(prod([2, 3, 4]))
