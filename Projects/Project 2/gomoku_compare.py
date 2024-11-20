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
        return {' ': 1, col: -2}.get(board[l[0]][l[1]], 0)  # normal, super false, opposite
    return 0

def is_bounded(board, y_end, x_end, length, d_y, d_x, col=None):
    beg_in = in_bounds(board, move(y_end, x_end, -length, d_y, d_x), col)
    end_in = in_bounds(board, move(y_end, x_end, 1, d_y, d_x), col)
    return "sus" if (beg_in + end_in) < 0 else {2: "OPEN", 1: "SEMIOPEN"}.get(beg_in + end_in, "CLOSED")

def detect_row(board, col, y_start, x_start, length, d_y, d_x, n_closed=False):
    direction_loops = {(0, 1): 8 - x_start, (1, 0): 8 - y_start, (1, 1): min(8 - x_start, 8 - y_start),
        (1, -1): min(1 + x_start, 8 - y_start)}
    loop = direction_loops.get((d_y, d_x), 0)
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
    if black != (0, 0, 0):
        return "Black won"
    elif white != (0, 0, 0):
        return "White won"
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