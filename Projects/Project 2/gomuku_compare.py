"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Nov. 1, 2023
"""





def move(y, x, inc, d_y, d_x):
    return [y + inc * d_y, x + inc * d_x]


def is_empty(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] != ' ':
                return False
    return True


def in_bounds(board, l, opp_stone):
    return (-1 < l[0] < 8 and -1 < l[1] < 8) and (board[l[0]][l[1]] != opp_stone)

def color_switch(board, y, x):
    return "w" if board[y][x] == "b" else "b"

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    opp_stone = color_switch(board, y_end, x_end)
    beg_in = in_bounds(board, move(y_end, x_end, -length, d_y, d_x), opp_stone)
    end_in = in_bounds(board, move(y_end, x_end, 1, d_y, d_x), opp_stone)
    return {2: "OPEN", 1: "SEMIOPEN"}.get(beg_in + end_in, "CLOSED")


# 0,0 0,1 0,2 0,3 0,4 0,5 0,6 0,7
# 1,0 1,1 1,2 1,3 1,4 1,5 1,6 1,7
# 2,0 2,1 2,2 2,3 2,4 2,5 2,6 2,7
# 3,0 3,1 3,2 3,3 3,4 3,5 3,6 3,7
# 4,0 4,1 4,2 4,3 4,4 4,5 4,6 4,7
# 5,0 5,1 5,2 5,3 5,4 5,5 5,6 5,7
# 6,0 6,1 6,2 6,3 6,4 6,5 6,6 6,7
# 7,0 7,1 7,2 7,3 7,4 7,5 7,6 7,7

# loop: last 1
# loop - 1: last 2
# loop - (length - 1): last length
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    l = [d_y, d_x]
    if l == [0, 1]:
        loop = 8 - x_start
    elif l == [1, 0]:
        loop = 8 - y_start
    elif l == [1, 1]:
        loop = min(8 - x_start, 8 - y_start)
    else:
        loop = min(1 + x_start, 8 - y_start)

    open_seq_count = 0
    semi_open_seq_count = 0
    for i in range(loop - length + 1):  # loop through the whole row
        start_square = move(y_start, x_start, i, d_y, d_x)
        count = 0
        for j in range(length):  # loop through each subset of len length inside of row
            new_square = move(start_square[0], start_square[1], j, d_y, d_x)
            if board[new_square[0]][new_square[1]] != col:
                break
            count += 1
        if count == length:
            now_square = move(start_square[0], start_square[1], length - 1, d_y, d_x)
            bounded_status = is_bounded(board, now_square[0], now_square[1], length, d_y, d_x)
            if bounded_status == "OPEN":
                open_seq_count += 1
            elif bounded_status == "SEMIOPEN":
                semi_open_seq_count += 1
    return open_seq_count, semi_open_seq_count


def sum_tuples(a,b):
    return tuple(sum(x) for x in zip(a, b))

# open_seq_count, semi_open_seq_count = 0, 0
def detect_rows(board, col, length):
    seq_vals = 0, 0
    for i in range(8):  # left to right and top to bottom
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, i, 0, length, 0, 1)) # l r
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, 0, i, length, 1, 0)) # t b
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, 0, i, length, 1, 1)) # 1 1
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, 0, i, length, 1, -1)) # 1 -1
    for i in range(1, 8):
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, i, 0, length, 1, 1)) # 1 1
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, i, 7, length, 1, -1)) # 1 -1
    return seq_vals


def search_max(board):
    max_score = -float('inf')
    best_move = None

    for y in range(8):
        for x in range(8):
            if board[y][x] == ' ':
                board[y][x] = 'b'
                current_score = score(board)
                board[y][x] = ' '  # Revert the board to its original state

                if current_score > max_score:
                    max_score = current_score
                    best_move = (y, x)

    return best_move


def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)

    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4]) + 500 * open_b[4] + 50 * semi_open_b[4] + -100 * open_w[3] + -30 *
            semi_open_w[3] + 50 * open_b[3] + 10 * semi_open_b[3] + open_b[2] + semi_open_b[2] - open_w[2] -
            semi_open_w[2])


def is_win(board):
    for col in ['b', 'w']:
        for y in range(8):
            for x in range(8):
                if x <= 3 and all(board[y][x + i] == col for i in range(5)):
                    return "Black won" if col == 'b' else "White won"
                if y <= 3 and all(board[y + i][x] == col for i in range(5)):
                    return "Black won" if col == 'b' else "White won"
                if x <= 3 and y <= 3 and all(board[y + i][x + i] == col for i in range(5)):
                    return "Black won" if col == 'b' else "White won"
                if x >= 4 and y <= 3 and all(board[y + i][x - i] == col for i in range(5)):
                    return "Black won" if col == 'b' else "White won"

    if all(board[y][x] != ' ' for y in range(8) for x in range(8)):
        return "Draw"
    return "Continue play"


def print_board(board):
    s = "*"
    for i in range(len(board[0]) - 1):
        s += str(i % 10) + "|"
    s += str((len(board[0]) - 1) % 10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i % 10)
        for j in range(len(board[0]) - 1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0]) - 1])

        s += "*\n"
    s += (len(board[0]) * 2 + 1) * "*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "] * sz)
    return board


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i)
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")


def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5
    x = 2
    d_x = 0
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3
    x = 5
    d_x = -1
    d_y = 1
    length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5
    x = 3
    d_x = -1
    d_y = 1
    length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


# ------------------------------- HELPER FUNCTION -------------------------------
def eval_test_case(fcn, fcn_in, l, correct_ans, show_board=1):
    # Create an empty 8x8 board
    board = make_empty_board(8)
    fcn = fcn.lower()

    # Place all the sequences on the board
    for seq in l:
        put_seq_on_board(board, *seq)

    # Define a dictionary to map function names to their corresponding functions and expected argument lengths
    function_map = {
        "is_bounded": (is_bounded, 5),
        "detect_row": (detect_row, 6),
        "detect_rows": (detect_rows, 2),
        "search_max": (search_max, 0)
    }

    # Check if the function name is valid
    if fcn in function_map:
        func, expected_args = function_map[fcn]
        if len(fcn_in) != expected_args:
            print("invalid no. of arguments")
            return
        else:
            your_ans = func(board, *fcn_in)
    else:
        print("invalid function")
        return

    # Check if the result matches the expected answer
    # ANSI escape codes for colors and formatting
    class Colors:
        OKGREEN = '\033[92m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    if your_ans == correct_ans:
        if show_board == 2:  # Always show the board if show_board is 2
            print_board(board)
        print(f"{Colors.OKGREEN}Test Case for {fcn} PASSED{Colors.ENDC}")
    else:
        if show_board == 1 or show_board == 2:  # Show the board if the test fails or if show_board is 2
            print_board(board)
        print(
            f"{Colors.FAIL}{Colors.BOLD}{Colors.UNDERLINE}Test Case for {fcn} FAILED. You returned \"{your_ans}\" instead of \"{correct_ans}\".{Colors.ENDC}")


# ------------------------------- CALL THIS TO TEST -------------------------------
def testing():
    # ------------------------------- TEST IS_BOUNDED -------------------------------
    eval_test_case("is_bounded", [3, 5, 3, 1, 0], [[1, 5, 1, 0, 3, "w"]], "OPEN")
    eval_test_case("is_bounded", [6, 1, 3, 1, 0], [[4, 1, 1, 0, 3, "w"]], "OPEN")
    l = [[3, 3, 0, 1, 3, "b"], [3, 6, 0, 1, 1, "w"]]
    eval_test_case("is_bounded", [3, 5, 3, 0, 1], l, "SEMIOPEN")
    l = [[3, 0, 0, 1, 4, "w"], [3, 4, 0, 1, 1, "b"]]
    eval_test_case("is_bounded", [3, 3, 4, 0, 1], l, "CLOSED")
    eval_test_case("is_bounded", [7, 2, 3, 1, 1], [[5, 0, 1, 1, 3, "b"]], "CLOSED")
    eval_test_case("is_bounded", [3, 3, 4, 1, -1], [[0, 6, 1, -1, 4, "w"]], "SEMIOPEN")
    # ------------------------------- TEST DETECT_ROW -------------------------------
    print()
    eval_test_case("detect_row", ["w", 0, 5, 3, 1, 0], [[1, 5, 1, 0, 3, "w"]], (1, 0))
    # ------------------------------- TEST DETECT_ROWS -------------------------------
    print()
    eval_test_case("detect_rows", ["w", 3], [[1, 5, 1, 0, 3, "w"]], (1, 0))
    # ------------------------------- TEST SEARCH_MAX -------------------------------
    print()
    l = [[0, 5, 1, 0, 4, "w"], [0, 6, 1, 0, 4, "b"]]
    eval_test_case("search_max", [], l, (4, 6))


if __name__ == '__main__':
    testing()