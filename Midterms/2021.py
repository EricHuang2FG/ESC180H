def print_even():
    for i in range(100, 201, 2):
        print(i)

def last_ind(L, e):
    for i in range(len(L) - 1, -1, -1):
        if L[i] == e:
            return i
    return None

def add_sparse_matrices(A, B, dim):
    matrix = []
    for i in range(dim[0]):
        row = []
        for j in range(dim[1]):
            val = 0
            if (i, j) in A:
                val += A[(i, j)]
            if (i, j) in B:
                val += B[(i, j)]
            row.append(val)
        matrix.append(row)
    return matrix

def smallest_common_multiple(a, b, c, d):
    for i in range(1, a * b * c * d + 1):
        if i % a == 0 and i % b == 0 and i % c == 0 and i % d == 0:
            return i

past_calls = []
def unlock(input):
    global past_calls
    past_calls.append(input)
    if len(past_calls) > 4:
        past_calls = past_calls[len(past_calls) - 4:]
    if past_calls == ["fall", "costumes", "costumes", "pumpkin"]:
        return "unlocked"
    return "locked"

def xyz_there(str):
  start = 0
  while True:
    i = str.find("xyz", start)
    if i == -1:
      return False
    start = i + 1
    if i == 0 or str[i - 1] != '.':
      return True

if __name__ == "__main__":
    print(xyz_there("abc.xyz"))
