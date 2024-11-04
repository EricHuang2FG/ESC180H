
"""
GENERAL INFORMATION:
The file already contains the starter code for the Gomoku game and AI engine (under INCLUDED FUNCTIONS). The program works as
follows. The computer (which plays with the black stones) always moves first. After the first move, the
user's and the computer's moves alternate. The computer determines its move by finding the move that
maximises the return value of the score function (which is provided).

Functions in gomoku.py accepts board as one of its arguments. This is the representation of the
Gomoku board. The square (y,x) on the board is stored in board[y][x]. The value of the square is:
Âˆ " ", if the square is empty,
Âˆ "b", if the square has a black stone on it, and
Âˆ "w", if the square has a white stone on it.

See the function printBoard for an example of using board.
An important part of the Gomoku AI engine is finding contiguous sequences of stones of the same colour
on the Gomoku board. 
There are four possible directions for a sequence: left-to-right, top-to-bottom,
upper-left-to-lower-right, and upper-right-to-lower-left. 
Note that we do NOT consider, for example, the direction right-lo-left, since a right-to-left sequence can be represented as a left-to-right sequence. The
direction of a sequence can be represented by a pair of numbers (d_y, d_x) as follows:
Âˆ (0,1): direction left-to-right. For example, the sequence of stones of the same colour on coordinates
(5,2), (5,3), (5,4), (5,5) is a sequence in direction left-to-right. Note that we say that the last
stone in the sequence is at location (5,5), not at location (5,2).
Âˆ (1,0): direction top-to-bottom. For example, a sequence of stones of the same colour on coordinates
(3,1), (4,1), (5,1) is a top-to-bottom sequence. Note that we say that the last stone in the
sequence is at location (5,1), not at location (3,1).
Âˆ (1,1): direction upper-left-to-lower-right. For example, a sequence of stones of the same colour on
coordinates (2,3), (3,4), (4,5) is an upper-left-to-lower-right sequence. Note that we say that
the last stone in the sequence is at location (4,5), not at location (2,3).
Âˆ (1,-1): direction upper-right-to-lower-left. For example, a sequence of stones of the same colour on
coordinates (5,5), (6,4), (7,3) is an upper-right-to-lower-left sequence. Note that we say that
the last stone in the sequence is at location (7,3), not at location (5,5).
A sequence can be:
Âˆ open: a stone can be put on a square at either side of the sequence.
Âˆ closed: the sequence is blocked on both sides, so that no stone can be placed on either side of the 
sequence. This can occur either because the sequence begins/ ends near the border of the board, or 
because there is a stone of a different colour in the location immediately next to the 
beginning/ end of the sequence. 
Âˆ semi-open: the sequence is neither open nor closed.

FIGURE 1: (1,0)
*0|1|2|3|4|5|6|7*
0 | | | | | | | *
1 | | | | | | | *
2 | | | | | | | *
3 | | | | | | | *
4 |w| | | | | | *
5 |w| | | | | | *
6 |w| | | | | | *
7 | | | | | | | *
*****************
An open sequence with 3 white stones. The direction is (1, 0). The last stone is at location (6,1).

FIGURE 2: (0,1)
*0|1|2|3|4|5|6|7*
0 | | | | | | | *
1 | | | | | | | *
2 | | | | | | | *
3 | | |b|b|b|w| *
4 | | | | | | | *
5 | | | | | | | *
6 | | | | | | | *
7 | | | | | | | *
*****************
A semi-open sequence with 3 black stones. The direction is (0,1). The last stone is at location (3,5).

FIGURE 3: (0,1)
*0|1|2|3|4|5|6|7*
0 | | | | | | | *
1 | | | | | | | *
2 | | | | | | | *
3w|w|w|w|b| | | *
4 | | | | | | | *
5 | | | | | | | *
6 | | | | | | | *
7 | | | | | | | *
*****************
A closed sequence with 4 white stones. The direction is (0,1). The last stone is at location (3,3). 

FIGURE 4: (1,1)
*0|1|2|3|4|5|6|7*
0 | | | | | | | *
1 | | | | | | | *
2 | | | | | | | *
3 | | | | | | | *
4 | | | | | | | *
5b| | | | | | | *
6 |b| | | | | | *
7 | |b| | | | | *
*****************
A closed sequence with 3 black stones. The direction is (1, 1). The last stone is at location (7,2).

FIGURE 5: (1,-1)
*0|1|2|3|4|5|6|7*
0 | | | | | |w| *
1 | | | | |w| | *
2 | | | |w| | | *
3 | | |w| | | | *
4 | | | | | | | *
5 | | | | | | | *
6 | | | | | | | *
7 | | | | | | | *
*****************
A semi-open sequence with 4 white stones. The direction is (1, -1). The last stone is at location (3,3).

"""
# ------------------------------- MY FUNCTIONS -------------------------------
def move(y, x, inc, d_y, d_x):
    """
    Calculate the new position on the board after moving a certain number of steps in a given direction.

    Parameters:
    y (int): The current y-coordinate on the board.
    x (int): The current x-coordinate on the board.
    inc (int): The number of steps to move.
    d_y (int): The change in the y-direction per step.
    d_x (int): The change in the x-direction per step.

    Returns:
    list: A list containing the new y and x coordinates after the move.
    """
    return [y + inc * d_y, x + inc * d_x]

def is_empty(board):
    """
    Check if the given Gomoku board is empty.

    This function iterates through an 8x8 board and checks if all positions are empty (represented by a space ' ').

    Parameters:
    board (list of list of str): A 2D list representing the Gomoku board, where each element is a string.

    Returns:
    bool: True if the board is empty, False otherwise.
    """
    for i in range(8):
        for j in range(8):
            if board[i][j] != ' ':
                return False
    return True

def in_board(l):
    """
    Check if the given coordinates are within the bounds of an 8x8 Gomoku board.

    This function checks if the provided coordinates (a list with two integers) are within the valid range of 0 to 7, inclusive.

    Parameters:
    l (list of int): A list containing two integers representing the coordinates on the board.

    Returns:
    bool: True if the coordinates are within the bounds of the board, False otherwise.
    """
    return -1 < l[0] < 8 and -1 < l[1] < 8

def in_bounds(board, l):
    """
    Check if the given coordinates are within the bounds of the board and the position is empty.

    This function first checks if the provided coordinates (a list with two integers) are within the valid range of the board using the `in_board` function. Then, it checks if the position on the board at these coordinates is empty (represented by a space ' ').

    Parameters:
    board (list of list of str): A 2D list representing the Gomoku board, where each element is a string.
    l (list of int): A list containing two integers representing the coordinates on the board.

    Returns:
    bool: True if the coordinates are within the bounds of the board and the position is empty, False otherwise.
    """
    return in_board(l) and (board[l[0]][l[1]] == ' ')

'''
REQUIREMENTS FOR IS_BOUNDED FUNCTION:
This function analyses the sequence of length length that ends at location (y end, x end). The function returns "OPEN" if the sequence is open, "SEMIOPEN" if the sequence if semi-open, and "CLOSED"
if the sequence is closed.
Assume that the sequence is complete (i.e., you are not just given a subsequence) and valid, and
contains stones of only one colour.
'''
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    beg_in = in_bounds(board, move(y_end, x_end, -length, d_y, d_x))
    end_in = in_bounds(board, move(y_end, x_end, 1, d_y, d_x))
    return {2: "OPEN", 1: "SEMIOPEN"}.get(beg_in + end_in, "CLOSED")

def ends(board, y_end, x_end, length, d_y, d_x):
    """
    Determine the status of the ends of a sequence of stones on the Gomoku board.

    This function analyzes the sequence of stones of a given length that ends at the specified coordinates
    (y_end, x_end) and moves in the direction specified by (d_y, d_x). It returns whether the sequence is
    "OPEN", "SEMIOPEN", or "CLOSED" based on the contents of the board at the ends of the sequence.

    Parameters:
    board (list of list of str): A 2D list representing the Gomoku board, where each element is a string.
    y_end (int): The y-coordinate of the end of the sequence.
    x_end (int): The x-coordinate of the end of the sequence.
    length (int): The length of the sequence.
    d_y (int): The change in the y-direction per step.
    d_x (int): The change in the x-direction per step.

    Returns:
    str: "OPEN" if the sequence is open, "SEMIOPEN" if the sequence is semi-open, and "CLOSED" if the sequence is closed.

    Notes:
    - The function assumes that the sequence is complete and valid, containing stones of only one color.
    - The function uses helper functions `move` and `in_board` to determine the positions and check if they are within the board boundaries.
    - The function considers the sequence to be "CLOSED" if either end of the sequence contains a stone of the same color as the sequence.
    - The function uses a dictionary to map the contents of the ends to the corresponding status ("OPEN", "SEMIOPEN", "CLOSED").
    """
    col = board[y_end][x_end]
    opp = "w" if col == "b" else "b"
    beg_content, end_content = 'o', 'o'
    beg_l = move(y_end, x_end, -length, d_y, d_x)
    end_l = move(y_end, x_end, 1, d_y, d_x)
    if in_board(beg_l):
        beg_content = board[beg_l[0]][beg_l[1]]
    if in_board(end_l):
        end_content = board[end_l[0]][end_l[1]]
    if beg_content == col or end_content == col:
        return "CLOSED"
    l = (min(beg_content, end_content), max(beg_content, end_content))
    dic = {(' ', ' '): "OPEN", (' ', 'o'): "SEMIOPEN", (' ', opp): "SEMIOPEN", ('o', 'o'): "CLOSED",
           ('o', opp): "CLOSED", (opp, 'o'): "CLOSED", (opp, opp): "CLOSED", }
    return dic[l]

'''
REQUIREMENTS FOR DETECT_ROW FUNCTION:
This function analyses the row (let's call it R) of squares that starts at the location (y_start,x_start)
and goes in the direction (d_y,d_x). Note that this use of the word row is different from â€œa row in
a tableâ€. Here, the word "row" means a sequence of squares, which are adjacent either horizontally,
or vertically, or diagonally. The function returns a tuple whose first element is the number of open
sequences of colour col of length length in the row R, and whose second element is the number of
semi-open sequences of colour col of length length in the row R.
Assume that (y_start,x_start) is located on the EDGE of the board. 
Only COMPLETE sequences count.
For example, column 1 in Fig. 1 is considered to contain one OPEN row of length 3, and NO other
rows.
Assume length is an integer greater or equal to 2
'''
def detect_row(board, col, y_start, x_start, length, d_y, d_x, n_closed=False):
    l = [d_y, d_x]
    if l == [0, 1]:
        loop = 8
        x_start = 0
    elif l == [1, 0]:
        loop = 8
        y_start = 0
    elif l == [1, 1]:
        y_temp = (y_start-x_start) if (y_start-x_start)>0 else 0
        x_temp = abs(y_start-x_start) if (y_start-x_start)<0 else 0
        y_start = y_temp
        x_start = x_temp
        loop = min(8 - x_start, 8 - y_start)
    else:
        y_temp = min(y_start,x_start)
        x_temp = max(y_start,x_start)
        y_start = y_temp
        x_start = x_temp
        loop = min(1 + x_start, 8 - y_start)
    open, semi, closed = 0, 0, 0
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
            bounded_status = ends(board, now_square[0], now_square[1], length, d_y, d_x)
            if bounded_status == "OPEN":
                open += 1
            elif bounded_status == "SEMIOPEN":
                semi += 1
            else:
                closed += 1
    return (open, semi, closed) if n_closed else (open, semi)


def sum_tuples(a, b):
    """
    Sums corresponding elements of two tuples.

    Args:
        a (tuple): The first tuple.
        b (tuple): The second tuple.

    Returns:
        tuple: A tuple containing the sums of the corresponding elements of `a` and `b`.

    Example:
        sum_tuples((1, 2, 3), (4, 5, 6))
        (5, 7, 9)
    """
    return tuple(sum(x) for x in zip(a, b))

'''
This function analyses the board board. The function returns a tuple, whose first element is the 
number of open sequences of colour col of length length on the entire board, and whose second element 
is the number of semi-open sequences of colour col of length length on the entire board. 
Only COMPLETE sequences count. For example, Fig. 1 is considered to contain one open row of length 3, 
and no other rows. 
Assume length is an integer greater or equal to 2.
'''
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

'''
This function uses the function score() (INCLUDED) to find the optimal move for black. It finds the
location (y,x), such that (y,x) is empty and putting a black stone on (y,x) maximizes the score of
the board as calculated by score(). The function returns a tuple (y, x) such that putting a black
stone in coordinates (y, x) maximizes the potential score (if there are several such tuples, you can
return any one of them). After the function returns, the contents of board must remain the same.
'''
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

'''
This function determines the current status of the game, and returns one of
["White won", "Black won", "Draw", "Continue playing"], depending on the current status
on the board. The only situation where "Draw" is returned is when board is full.
'''
def is_win(board):
    white = 0, 0, 0
    black = 0, 0, 0
    for i in range(5, 9):
        white = sum_tuples(white, detect_rows(board, "w", i, True))
        black = sum_tuples(black, detect_rows(board, "b", i, True))
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

"""
This included function adds the sequence of stones of colour col of length length to board, 
starting at location (y,x) and moving in the direction (d_y, d_x).
"""
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x

# ------------------------------- HELPER FUNCTIONS -------------------------------
def eval_test_case(fcn, fcn_in, l, correct_ans, show_board=1):
    # if show_board is: 0 -> never show board, 1 -> show board if wrong ans
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
    eval_test_case("is_bounded", [3, 5, 3, 1, 0], [[1, 5, 1, 0, 3, "w"]], "OPEN")
    eval_test_case("is_bounded", [6, 1, 3, 1, 0], [[4, 1, 1, 0, 3, "w"]], "OPEN")
    l = [[3, 3, 0, 1, 3, "b"], [3, 6, 0, 1, 1, "w"]]
    eval_test_case("is_bounded", [3, 5, 3, 0, 1], l, "SEMIOPEN")
    l = [[3, 0, 0, 1, 4, "w"], [3, 4, 0, 1, 1, "b"]]
    eval_test_case("is_bounded", [3, 3, 4, 0, 1], l, "CLOSED")
    eval_test_case("is_bounded", [7, 2, 3, 1, 1], [[5, 0, 1, 1, 3, "b"]], "CLOSED")
    eval_test_case("is_bounded", [3, 3, 4, 1, -1], [[0, 6, 1, -1, 4, "w"]], "SEMIOPEN")

    eval_test_case("detect_row", ["w", 0, 5, 3, 1, 0], [[1, 5, 1, 0, 3, "w"]], (1, 0))

    eval_test_case("detect_rows", ["w", 3], [[1, 5, 1, 0, 3, "w"]], (1, 0))

    l = [[0, 5, 1, 0, 4, "w"], [0, 6, 1, 0, 4, "b"]]
    eval_test_case("search_max", [], l, (4, 6))

    l = [[0, 7, 0, 1, 1, 'w'], [5, 7, 1, -1, 3, 'b'], [1, 6, 1, -1, 1, 'w']]
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

    # eval_test_case("detect_rows", [?], l, (?))
    # eval_test_case("search_max", [], l, (?))

    l = [[3, 2,0, 1, 2, 'b']]
    eval_test_case("detect_row", ['b', 3, 0, 2, 0, 1], l, (1, 0)) 

    l = [[2, 5, 1, 0, 3, 'w']]
    eval_test_case("detect_row", ['w', 0, 5, 3, 1, 0], l, (1, 0))

    l = [[1, 1, 1, 1, 4, 'b']]
    eval_test_case("detect_row", ['b', 0, 0, 4, 1, 1], l, (1, 0))

    l = [[5, 2, 0, 1, 3, 'w'],[5,5,0,1,1,'b']]
    eval_test_case("detect_row", ['w', 5, 0, 3, 0, 1], l, (0, 1))

    l = [[1, 6, 1, 0, 2, 'b'],[0,6,0,1,1,'w'],[3,6,0,1,1,'w']]
    eval_test_case("detect_row", ['b', 0, 6, 2, 1, 0], l, (0, 0))

    l = [[0, 7, 1, -1, 3, 'w']]
    eval_test_case("detect_row", ['w', 0, 7, 3, 1, -1], l, (0, 1))

    l = [[7, 1, 0, 1, 2, 'b'],[7,0,0,1,1,'w']]
    eval_test_case("detect_row", ['b', 7, 0, 2, 0, 1], l, (0, 1))

    l = [[0, 0, 1, 1, 2, 'w'],[2,2,0,1,1,'b']]
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

    l = [[3, 3, 0, 1, 3, 'b'],[3,2,0,1,1,'w'],[3,6,0,1,1,'w']]
    eval_test_case("detect_row", ['b', 3, 7, 3, 0, 1], l, (0, 0))

    l = [[0, 7, 1, -1, 8, 'w']]
    eval_test_case("detect_row", ['w', 0, 1, 1, 1, 1], l, (1, 0))
    eval_test_case("detect_row", ['w', 0, 7, 1, 1, 1], l, (0, 0))

    l = [[4, 0, 0, 1, 2, 'b'],[4,2,0,1,1,'w']]  
    eval_test_case("detect_row", ['b', 4, 0, 3, 0, 1], l, (0, 0))

    l = [[0, 2, 1, 0, 2, 'b']]
    eval_test_case("detect_row", ['b', 0, 2, 2, 1, 0], l, (0, 1))

    l = [[2, 5, 1, -1, 3, 'w'],[1,6,0,1,1,'b']]
    eval_test_case("detect_row", ['w', 0, 7, 3, 1, -1], l, (0, 1))
    eval_test_case("detect_row", ['w', 7, 0, 3, 1, -1], l, (0, 1))

    l = [[3, 3, 1, 0, 5, 'b']]
    eval_test_case("detect_row", ['b', 0, 3, 5, 1, 0], l, (0, 1))

    l = [[5, 5, 1, 1, 2, 'b'],[5, 6, 1, 1, 1, 'b']]
    eval_test_case("detect_row", ['b', 7, 7, 2, 1, 1], l, (1,0))
    eval_test_case("detect_row", ['b', 0, 6, 2, 1, 0], l, (1,0))

    
    # 1. Open sequence in the middle of the board (Horizontal)
    l = [[4, 2, 0, 1, 3, 'b']]  # Sequence starting at (4,2) moving right
    eval_test_case("is_bounded", [4, 4, 3, 0, 1], l, "OPEN")
    
    # 2. Semi-open sequence at the edge of the board (Vertical)
    l = [[0, 5, 1, 0, 4, 'w']]  # Sequence starting at (0,5) moving down
    eval_test_case("is_bounded", [3, 5, 4, 1, 0], l, "SEMIOPEN")
    
    # 3. Closed sequence blocked by opposite color (Diagonal)
    l = [
        [2, 2, 1, 1, 5, 'b'],    # Sequence starting at (2,2) moving down-right
        [1, 1, 0, 0, 1, 'w'],    # Blocking stone at (1,1)
        [7, 7, 0, 0, 1, 'w']     # Blocking stone at (7,7)
    ]
    eval_test_case("is_bounded", [6, 6, 5, 1, 1], l, "CLOSED")
    
    # 4. Closed sequence blocked by same color
    l = [
        [4, 2, 0, 1, 3, 'b'],    # Sequence starting at (4,2) moving right
        [4, 5, 0, 0, 1, 'b'],    # Blocking stone at (4,5)
        [4, 1, 0, 0, 1, 'b']     # Blocking stone at (4,1)
    ]
    eval_test_case("is_bounded", [4, 4, 3, 0, 1], l, "CLOSED")
    
    # 5. Semi-open sequence at board edge and blocked (Diagonal)
    l = [
        [7, 0, -1, 1, 3, 'w'],   # Sequence starting at (7,0) moving up-right
        [4, 3, 0, 0, 1, 'b']     # Blocking stone at (4,3)
    ]
    eval_test_case("is_bounded", [7, 0, 3, 1, -1], l, "CLOSED")
    
    # 6. Open sequence near the edge (Vertical)
    l = [[1, 7, 1, 0, 2, 'b']]  # Sequence starting at (1,7) moving down
    eval_test_case("is_bounded", [2, 7, 2, 1, 0], l, "OPEN")
    
    # 7. Closed sequence at the corner blocked by opposite color
    l = [
        [0, 0, 1, 1, 2, 'w'],    # Sequence starting at (0,0) moving down-right
        [2, 2, 0, 0, 1, 'b']
    ]
    eval_test_case("is_bounded", [1, 1, 2, 1, 1], l, "CLOSED")
    
    # 8. Open sequence along the main diagonal
    l = [[0, 7, 1, -1, 3, 'b']] # Sequence starting at (0,7) moving down-left
    eval_test_case("is_bounded", [2, 5, 3, 1, -1], l, "SEMIOPEN")
    
    # 9. Semi-open sequence with one end at the border
    l = [[7, 3, -1, 0, 3, 'w']] # Sequence starting at (7,3) moving up
    eval_test_case("is_bounded", [7, 3, 3, 1, 0], l, "SEMIOPEN")
    
    # 10. Closed sequence entirely at the edge
    l = [[0, 5, 0, 1, 3, 'b']]  # Sequence starting at (0,5) moving right
    eval_test_case("is_bounded", [0, 7, 3, 0, 1], l, "SEMIOPEN")

# testing()