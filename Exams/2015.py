def x_won(board):
    pass

def x_can_win(board): # this is WRONG!!! You should in fact do mutual recursion, hmmmm
    # first make a manual deepcopy of board
    board_copy = []
    for row in board:
        new_row = []
        for element in row:
            new_row.append(element)
        board_copy.append(new_row)
    
    # put X in each empty space of the board and see if X can win
    for i, row in enumerate(board_copy):
        for j, element in enumerate(row):
            if element == " ":
                board_copy[i][j] = "X"
                if x_won(board_copy):
                    return True
                board_copy[i][j] = " "
    return False

def merge(L1, L2):
    if len(L1) == 0:
        return L2
    if len(L2) == 0:
        return L1
    if L1[0] < L2[0]:
        return [L1[0]] + merge(L1[1:], L2)
    return [L2[0]] + merge(L1, L2[1:])

def movies_by_release_date(movies):
    # method 1, using selection sort
    movies_sorted = []
    while len(movies_sorted) < len(movies):
        max_key, max_value = "", -999
        for movie, description in movies.items():
            if movie in movies_sorted:
                continue
            date, _ = description.split(", ")
            date = -888 if date == "a long time ago" else int(date)
            if date > max_value:
                max_value = date
                max_key = movie
        movies_sorted.append(max_key)
    return movies_sorted

def movies_by_release_date_method_2(movies):
    # method 2, using sorted()
    for key, value in movies.items():
        date, _ = value.split(", ")
        date = -999 if date == "a long time ago" else int(date)
        movies[key] = date
    movies = sorted(movies.items(), key=lambda item: item[1], reverse=True)
    return [tup[0] for tup in movies]

def euc_distance(u, v):
    tot = 0
    for i in range(1, max(max(u.keys()), max(v.keys()))):
        ui = u.get(i) or 0
        vi = v.get(i) or 0
        tot += (ui - vi) ** 2
    return tot ** (1 / 2)

# question 8

# a) merge L1 and L2 and sorts them in reverse
# b) traversing through the array, it slices two lists from L of length i and sorts their merged array in reverse order using mystery_helper
#    , where i is 1, 2, 4, 8, ... For example, if the array is [1, 2, 3, 4, 5, 6, 7], it first takes [1] and [2] and sort
#    their combined version reversed, then, the loop pointer moves forwards and it sorts (in the same manner) the combination of
#    the lists [3, 4] and [5, 6]
# c) O(n^2)