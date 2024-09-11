import math

# question 1
def get_perfect_squares(n):
    result = []
    for i in range(math.floor(math.sqrt(n)) + 1):
        result.append(pow(i, 2))
    return result

if __name__ == "__main__":
    print(get_perfect_squares(5))