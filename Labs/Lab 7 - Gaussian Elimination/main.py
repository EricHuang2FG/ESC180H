import numpy as np

def print_matrix(M_lol: list) -> None:
    print(np.array(M_lol))

def get_lead_ind(row: list) -> int:
    for index, value in enumerate(row):
        if value != 0:
            return index

def get_row_to_swap(M: list, start_i: int) -> int:
    col_index, row_index = len(M[0]), 0
    for i in range(start_i, len(M)):
        row = M[i]
        for j, val in enumerate(row):
            if val != 0 and j < col_index:
                col_index = j
                row_index = i
                break
    return row_index

def add_rows_coefs(r1: list, c1: int, r2: list, c2: int) -> list:
    return [r1[i] * c1 + r2[i] * c2 for i in range(len(r1))]

def eliminate(M: list, row_to_sub: int, best_lead_ind: int, forward: bool) -> None:
    start, end = (row_to_sub + 1, len(M)) if forward else (0, row_to_sub)
    for i in range(start, end):
        M[i] = add_rows_coefs(M[row_to_sub], -M[i][best_lead_ind] / M[row_to_sub][best_lead_ind], M[i], 1)

def forward_step(M: list) -> None:
    for i, _ in enumerate(M):
        swap_index = get_row_to_swap(M, i)
        M[i], M[swap_index] = M[swap_index], M[i]
        best_leading_index = get_lead_ind(M[i])
        for row in M[i + 1:]:
            best_leading_index = min(best_leading_index, get_lead_ind(row))
        eliminate(M, i, best_leading_index, True)
        print_matrix(M)

def backward_step(M: list) -> None:
    for i in range(len(M) - 1, -1, -1):
        eliminate(M, i, get_lead_ind(M[i]), False)
        print_matrix(M)
    for _, row in enumerate(M):
        leading_coefficient = row[get_lead_ind(row)]
        for k, _ in enumerate(row):
            row[k] /= leading_coefficient
    print_matrix(M)

def solve(M: list, b: list):
    for index, row in enumerate(M):
        row.append(b[index])
    forward_step(M)
    backward_step(M)
    print_matrix(M)
    x = [row[len(row) - 1] for row in M]
    print(x)

if __name__ == "__main__":
    A = [[0, 0, 1, 0, 2],
         [1, 0, 2, 3, 4],
         [3, 0, 4, 2, 1],
         [1, 0, 1, 1, 2]]
    B = [[1, -2, 3, 22],
         [3, 10, 1, 314],
         [1, 5, 3, 92]]
    r1, c1 = [1, 3, 4], 2
    r2, c2 = [3, 2, 4], 3
    forward_step(B)
    backward_step(B)
    M1 = [[2, 1],
          [1, 3]]
    M2 = [8, 10]
    solve(M1, M2)
