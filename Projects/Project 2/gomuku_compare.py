# ------------------------------- MY FUNCTIONS -------------------------------
def is_empty(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] != ' ': return False
    return True

def move(y, x, inc, d_y, d_x):
    return [y + inc * d_y, x + inc * d_x]

def in_bounds(board, l, col='x'):
    if -1 < l[0] < 8 and -1 < l[1] < 8:  # in the board (not out of bounds)
        return { ' ': 1, col: -2 }.get(board[l[0]][l[1]], 0) #normal, super false, opposite
    return 0

def is_bounded(board, y_end, x_end, length, d_y, d_x, col=None):
    beg_in = in_bounds(board, move(y_end, x_end, -length, d_y, d_x), col)
    end_in = in_bounds(board, move(y_end, x_end, 1, d_y, d_x), col)
    return "sus" if (beg_in + end_in) < 0 else {2: "OPEN", 1: "SEMIOPEN"}.get(beg_in + end_in, "CLOSED")

def detect_row(board, col, y_start, x_start, length, d_y, d_x, n_closed=False):
    l = [d_y, d_x]
    if l == [0, 1]:
        loop = 8
        x_start = 0
    elif l == [1, 0]:
        loop = 8
        y_start = 0
    elif l == [1, 1]:
        delta = y_start - x_start
        y_start, x_start = max(delta, 0), max(-delta, 0)
        loop = min(8 - x_start, 8 - y_start)
    else:
        y_start, x_start = min(y_start, x_start), max(y_start, x_start)
        loop = min(1 + x_start, 8 - y_start)
    o_seq, s_seq, c_seq = 0, 0, 0
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
            bounded_status = is_bounded(board, now_square[0], now_square[1], length, d_y, d_x,
                                        board[now_square[0]][now_square[1]])
            if bounded_status == "OPEN":
                o_seq += 1
            elif bounded_status == "SEMIOPEN":
                s_seq += 1
            elif bounded_status == "CLOSED":
                c_seq += 1
    return (o_seq, s_seq, c_seq) if n_closed else (o_seq, s_seq)

def sum_tuples(a, b):
    return tuple(sum(x) for x in zip(a, b))

def detect_rows(board, col, length, closed=False):
    seq_vals = 0, 0, 0
    for i in range(8):  # left to right and top to bottom
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, i, 0, length, 0, 1, closed))  # l r
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, 0, i, length, 1, 0, closed))  # t b
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, 0, i, length, 1, 1, closed))  # 1 1
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, 0, i, length, 1, -1, closed))  # 1 -1
    for i in range(1, 8):
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, i, 0, length, 1, 1, closed))  # 1 1
        seq_vals = sum_tuples(seq_vals, detect_row(board, col, i, 7, length, 1, -1, closed))  # 1 -1
    return seq_vals if closed else seq_vals[:2]

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

def is_win(board):
    white = sum_tuples((0, 0, 0), detect_rows(board, "w", 5, True))
    black = sum_tuples((0, 0, 0), detect_rows(board, "b", 5, True))
    if white != (0, 0, 0):
        return "White won"
    elif black != (0, 0, 0):
        return "Black won"
    elif all(board[y][x] != ' ' for y in range(8) for x in range(8)):
        return "Draw"
    return "Continue playing"

# ------------------------------- INCLUDED FUNCTIONS -------------------------------
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

# ------------------------------- HELPER FUNCTIONS -------------------------------
def eval_test_case(fcn, fcn_in, l, correct_ans, show_board=1):
    # if show_board is: 0 -> never show board, 1 -> show board if wrong answer
    # Create an empty 8x8 board
    board = make_empty_board(8)
    fcn = fcn.lower()

    # Place all the sequences on the board
    for seq in l:
        put_seq_on_board(board, *seq)

    # Define a dictionary to map function names to their corresponding functions and expected argument lengths
    function_map = {"is_bounded": (is_bounded, 5), "detect_row": (detect_row, 6), "detect_rows": (detect_rows, 2),
                    "search_max": (search_max, 0), "is_win": (is_win, 0)}

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

    # ANSI escape codes for colors and formatting
    class Colors:
        OKGREEN = '\033[92m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    # Check if the result matches the expected answer
    if your_ans == correct_ans:
        if show_board == 2:  # Always show the board if show_board is 2
            print_board(board)
            print(f"l = {l}")
            print(f"fcn_input_args: {fcn_in}")
            print(f"correct ans: {correct_ans}")
        print(f"{Colors.OKGREEN}Test Case for {fcn} PASSED{Colors.ENDC}")
    else:
        if show_board == 1 or show_board == 2:  # Show the board if the test fails or if show_board is 2
            print("----V----V----V----V----V----V----V----V----V----V----")
            print_board(board)
            print(f"l = {l}")
            print(f"fcn_input_args: {fcn_in}")

        print(
            f"{Colors.FAIL}{Colors.BOLD}{Colors.UNDERLINE}Test Case for {fcn} FAILED. You returned \"{your_ans}\" instead of \"{correct_ans}\".{Colors.ENDC}")
        if show_board == 1 or show_board == 2:
            print("----^----^----^----^----^----^----^----^----^----^----")

def testing():
    print("----------IS_BOUNDED TESTS----------")
    eval_test_case("is_bounded", [3, 5, 3, 1, 0], [[1, 5, 1, 0, 3, "w"]], "OPEN")
    eval_test_case("is_bounded", [6, 1, 3, 1, 0], [[4, 1, 1, 0, 3, "w"]], "OPEN")
    l = [[3, 3, 0, 1, 3, "b"], [3, 6, 0, 1, 1, "w"]]
    eval_test_case("is_bounded", [3, 5, 3, 0, 1], l, "SEMIOPEN")
    l = [[3, 0, 0, 1, 4, "w"], [3, 4, 0, 1, 1, "b"]]
    eval_test_case("is_bounded", [3, 3, 4, 0, 1], l, "CLOSED")
    eval_test_case("is_bounded", [7, 2, 3, 1, 1], [[5, 0, 1, 1, 3, "b"]], "CLOSED")
    eval_test_case("is_bounded", [3, 3, 4, 1, -1], [[0, 6, 1, -1, 4, "w"]], "SEMIOPEN")
    l = [[4, 2, 0, 1, 3, 'b']]  # Sequence starting at (4,2) moving right
    eval_test_case("is_bounded", [4, 4, 3, 0, 1], l, "OPEN")
    l = [[0, 5, 1, 0, 4, 'w']]  # Sequence starting at (0,5) moving down
    eval_test_case("is_bounded", [3, 5, 4, 1, 0], l, "SEMIOPEN")
    l = [[2, 2, 1, 1, 5, 'b'], [1, 1, 0, 0, 1, 'w'], [7, 7, 0, 0, 1, 'w']]
    eval_test_case("is_bounded", [6, 6, 5, 1, 1], l, "CLOSED")
    l = [[4, 2, 0, 1, 3, 'b'], [4, 5, 0, 0, 1, 'b'], [4, 1, 0, 0, 1, 'b']]
    eval_test_case("is_bounded", [4, 4, 3, 0, 1], l, "CLOSED")
    l = [[7, 0, -1, 1, 3, 'w'], [4, 3, 0, 0, 1, 'b']]
    eval_test_case("is_bounded", [7, 0, 3, 1, -1], l, "CLOSED")
    l = [[1, 7, 1, 0, 2, 'b']]  # Sequence starting at (1,7) moving down
    eval_test_case("is_bounded", [2, 7, 2, 1, 0], l, "OPEN")
    l = [[0, 0, 1, 1, 2, 'w'], [2, 2, 0, 0, 1, 'b']]
    eval_test_case("is_bounded", [1, 1, 2, 1, 1], l, "CLOSED")
    l = [[0, 7, 1, -1, 3, 'b']]
    eval_test_case("is_bounded", [2, 5, 3, 1, -1], l, "SEMIOPEN")
    l = [[7, 3, -1, 0, 3, 'w']]
    eval_test_case("is_bounded", [7, 3, 3, 1, 0], l, "SEMIOPEN")
    l = [[0, 5, 0, 1, 3, 'b']]
    eval_test_case("is_bounded", [0, 7, 3, 0, 1], l, "SEMIOPEN")
    print("----------DETECT_ROW TESTS----------")
    eval_test_case("detect_row", ["w", 0, 5, 3, 1, 0], [[1, 5, 1, 0, 3, "w"]], (1, 0))
    l = [[3, 2, 0, 1, 2, 'b']]
    eval_test_case("detect_row", ['b', 3, 0, 2, 0, 1], l, (1, 0))
    l = [[2, 5, 1, 0, 3, 'w']]
    eval_test_case("detect_row", ['w', 0, 5, 3, 1, 0], l, (1, 0))
    l = [[1, 1, 1, 1, 4, 'b']]
    eval_test_case("detect_row", ['b', 0, 0, 4, 1, 1], l, (1, 0))
    l = [[5, 2, 0, 1, 3, 'w'], [5, 5, 0, 1, 1, 'b']]
    eval_test_case("detect_row", ['w', 5, 0, 3, 0, 1], l, (0, 1))
    l = [[1, 6, 1, 0, 2, 'b'], [0, 6, 0, 1, 1, 'w'], [3, 6, 0, 1, 1, 'w']]
    eval_test_case("detect_row", ['b', 0, 6, 2, 1, 0], l, (0, 0))
    l = [[0, 7, 1, -1, 3, 'w']]
    eval_test_case("detect_row", ['w', 0, 7, 3, 1, -1], l, (0, 1))
    l = [[7, 1, 0, 1, 2, 'b'], [7, 0, 0, 1, 1, 'w']]
    eval_test_case("detect_row", ['b', 7, 0, 2, 0, 1], l, (0, 1))
    l = [[0, 0, 1, 1, 2, 'w'], [2, 2, 0, 1, 1, 'b']]
    eval_test_case("detect_row", ['w', 0, 0, 2, 1, 1], l, (0, 0))
    l = [[4, 4, 0, 1, 3, 'b']]
    eval_test_case("detect_row", ['b', 4, 7, 3, 0, 1], l, (1, 0))
    eval_test_case("detect_row", ['b', 4, 0, 2, 0, 1], l, (0, 0))
    l = [[4, 1, 1, 1, 3, 'w']]
    eval_test_case("detect_row", ['w', 3, 0, 2, 1, 1], l, (0, 0))
    l = [[1, 0, 0, 1, 5, 'b']]
    eval_test_case("detect_row", ['b', 1, 0, 5, 0, 1], l, (0, 1))
    l = [[0, 5, 1, 0, 2, 'w']]
    eval_test_case("detect_row", ['w', 0, 5, 2, 1, 0], l, (0, 1))
    eval_test_case("detect_row", ['w', 7, 5, 2, 1, 0], l, (0, 1))
    l = [[3, 3, 0, 1, 3, 'b'], [3, 2, 0, 1, 1, 'w'], [3, 6, 0, 1, 1, 'w']]
    eval_test_case("detect_row", ['b', 3, 7, 3, 0, 1], l, (0, 0))
    l = [[0, 7, 1, -1, 8, 'w']]
    eval_test_case("detect_row", ['w', 0, 1, 1, 1, 1], l, (1, 0))
    eval_test_case("detect_row", ['w', 0, 7, 1, 1, 1], l, (0, 0))
    l = [[4, 0, 0, 1, 2, 'b'], [4, 2, 0, 1, 1, 'w']]
    eval_test_case("detect_row", ['b', 4, 0, 3, 0, 1], l, (0, 0))
    l = [[0, 2, 1, 0, 2, 'b']]
    eval_test_case("detect_row", ['b', 0, 2, 2, 1, 0], l, (0, 1))
    l = [[2, 5, 1, -1, 3, 'w'], [1, 6, 0, 1, 1, 'b']]
    eval_test_case("detect_row", ['w', 0, 7, 3, 1, -1], l, (0, 1))
    eval_test_case("detect_row", ['w', 7, 0, 3, 1, -1], l, (0, 1))
    l = [[3, 3, 1, 0, 5, 'b']]
    eval_test_case("detect_row", ['b', 0, 3, 5, 1, 0], l, (0, 1))
    l = [[5, 5, 1, 1, 2, 'b'], [5, 6, 1, 1, 1, 'b']]
    eval_test_case("detect_row", ['b', 7, 7, 2, 1, 1], l, (1, 0))
    eval_test_case("detect_row", ['b', 0, 6, 2, 1, 0], l, (1, 0))
    print("----------DETECT_ROWS/SEARCH_MAX TESTS----------")
    eval_test_case("detect_rows", ["w", 3], [[1, 5, 1, 0, 3, "w"]], (1, 0))
    l = [[0, 5, 1, 0, 4, "w"], [0, 6, 1, 0, 4, "b"]]
    eval_test_case("search_max", [], l, (4, 6))
    l = [[5, 7, 1, -1, 3, 'b'], [0, 7, 1, -1, 2, 'w']]
    eval_test_case("detect_rows", ["b", 3], l, (0, 0))
    eval_test_case("search_max", [], l, (5, 6))
    l = [[1, 3, 1, 1, 3, 'b'], [2, 6, 1, 0, 3, 'w']]
    eval_test_case("detect_rows", ['b', 7], l, (0, 0))
    eval_test_case("search_max", [], l, (1, 6))
    l = [[5, 6, 0, 1, 1, 'b']]
    eval_test_case("detect_rows", ['w', 3], l, (0, 0))
    eval_test_case("search_max", [], l, (4, 5))
    l = [[5, 1, 1, 1, 2, 'b'], [4, 0, 1, 1, 2, 'w'], [4, 5, 0, 1, 3, 'b'], [5, 5, 1, 0, 2, 'b']]
    eval_test_case("detect_rows", ['b', 2], l, (1, 0))
    eval_test_case("search_max", [], l, (3, 5))
    print("----------IS_WIN TESTS----------")
    l = [[0, 0, 1, 1, 5, 'b']]
    eval_test_case("is_win", [], l, "Black won")
    l = [[0, 0, 1, 1, 6, 'b']]
    eval_test_case("is_win", [], l, "Continue playing")
    l = [[0, 0, 1, 1, 7, 'b']]
    eval_test_case("is_win", [], l, "Continue playing")
    l = [[0, 0, 1, 1, 8, 'b']]
    eval_test_case("is_win", [], l, "Continue playing")

# testing()