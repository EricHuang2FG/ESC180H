'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

from random import randint
from copy import deepcopy
from time import sleep

def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3 * i + 1)  + " | " + str(3 * i + 2)  + " | " +  str(3 * i + 3) 
        print(line1 + " " * 5 + line2)
        if i < 2:
            print("---+---+---" + " " * 5 + "---+---+---")
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "] * 3)
    return board

def get_coords(square_num: int) -> list:
    if square_num <= 0 or square_num > 9:
        return print("Must be an integer between (inclusive) 1 and 9")
    # coord goes like [y, x]
    coord = [None, None]
    if square_num <= 3:
        coord[0] = 0
    elif square_num >= 4 and square_num <= 6:
        coord[0] = 1
    else:
        coord[0] = 2
    if square_num in [1, 4, 7]:
        coord[1] = 0
    elif square_num in [2, 5, 8]:
        coord[1] = 1
    else:
        coord[1] = 2
    return coord

def put_in_board(board: list, mark: str, square_num: int) -> None:
    coord = get_coords(square_num)
    if board[coord[0]][coord[1]] == " ":
        board[coord[0]][coord[1]] = mark
    else:
        print("Already occupied!!")

def get_free_squares(board: list) -> list:
    all_free_squares = []
    for i, sub in enumerate(board):
        for j, value in enumerate(sub):
            if value == " ":
                all_free_squares.append([i, j])
    return all_free_squares

def bot_make_move(board: list, mark: str) -> None:
    free_squares = get_free_squares(board)
    if len(free_squares) == 0:
        return print("No more free squares!!!")
    # check if it can immediately win
    for free_square in free_squares:
        dummy_board = deepcopy(board)
        dummy_board[free_square[0]][free_square[1]] = mark
        if is_win(dummy_board, mark):
            board[free_square[0]][free_square[1]] = mark
            return
    # make a random move and see if the player can immediately win, if so just take that spot
    dummy_board = deepcopy(board)
    coord = free_squares[randint(0, len(free_squares) - 1)]
    dummy_board[coord[0]][coord[1]] = mark
    free_squares = get_free_squares(dummy_board)
    coord_to_steal = None
    for free_square in free_squares:
        dummy_dummy_board = deepcopy(dummy_board)
        dummy_dummy_board[free_square[0]][free_square[1]] = "X"
        if is_win(dummy_dummy_board, "X"):
            coord_to_steal = free_square
            break
    if coord_to_steal: # if the player can immediately win, we take that spot
        coord = coord_to_steal
    board[coord[0]][coord[1]] = mark

def is_row_all_marks(board: list, row_i: int, mark: str) -> bool:
    row = board[row_i]
    return len(set(row)) == 1 and row[0] == mark

def is_col_all_marks(board: list, col_i: int, mark: str) -> bool:
    col = [board[0][col_i], board[1][col_i], board[2][col_i]]
    return len(set(col)) == 1 and col[0] == mark

def is_diagonal_all_marks(board: list, mark: str) -> bool:
    return ((board[0][0] == mark and board[0][0] == board[1][1] == board[2][2]) or
        (board[0][2] == mark and board[0][2] == board[1][1] == board[2][0])
    )

def is_win(board: list, mark: str) -> bool:
    for i in range(3):
        if is_col_all_marks(board, i, mark) or is_row_all_marks(board, i, mark):
            return True
    return is_diagonal_all_marks(board, mark)
    
if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    
    print_board_and_legend(board)
    
    count = 0
    val = ""
    # COMMENTED OUT BELOW IS PLAYER VS. PLAYER  CODE
    # while True:
    #     val = input("Enter your move: ")
    #     if val == "END":
    #         break
    #     try:
    #         val = int(val)
    #     except ValueError:
    #         print("Please enter a number from 1 to 9")
    #         continue
    #     mark = "X" if count % 2 == 0 else "0"
    #     put_in_board(board, mark, val)
    #     print_board_and_legend(board)
    #     count += 1

    while True:
        if count % 2 == 0:
            val = input("Enter your move: ")
            if val == "END":
                break
            try:
                val = int(val)
            except ValueError:
                print("Please enter a number from 1 to 9")
                continue
            put_in_board(board, "X", val)
            if is_win(board, "X"):
                print("\n\n\nThe player won! The result is: ")
                print_board_and_legend(board)
                break
        else:
            print("The AI makes a move: ")
            bot_make_move(board, "0")
            if is_win(board, "0"):
                print("\n\n\nThe AI won! The result is: ")
                print_board_and_legend(board)
                break
        print_board_and_legend(board)
        sleep(0.5)
        count += 1
