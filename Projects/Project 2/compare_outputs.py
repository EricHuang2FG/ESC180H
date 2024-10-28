from gomuku import (
    is_empty,
    detect_rows,
    search_max,
    is_win
)
import gomuku_compare as test
from random import randint

suceeded_test_count, failed_test_count = 0, 0

def print_board(board: list, f) -> None:
    s = "*"
    for i in range(len(board[0]) - 1):
        s += " " + str(i % 10) + " " if i == 0 else str(i % 10) + " "
    s += str((len(board[0])-1)%10)
    s += " *\n"
    
    for i in range(len(board)):
        s += str(i % 10) + "|"
        for j in range(len(board[0]) - 1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0]) - 1]) 
        s += "|*\n"
    s += (len(board[0]) * 2 + 1) * "*" + "**\n\n"
    f.write(s)

def generate_board() -> list:
    sample = ['w', ' ', ' ', ' ', 'b', ' ']
    if randint(1, 100) <= 10: # generate empty board
        board = [[' ' for _ in range(8)] for _ in range(8)]
    else:
        board = [[sample[randint(0, 5)] for _ in range(8)] for _ in range(8)]
    return board

def assert_test_result(function: str, args: str, output_a: str, output_b: str, f) -> None:
    global suceeded_test_count, failed_test_count
    s = f"Function call: {function}({args})\nLocal output: {output_a}\nCompared output: {output_b}\nComparison "
    if output_a == output_b:
        suceeded_test_count += 1
        s += "SUCEEDED ✅✅✅✅✅✅\n\n\n"
    else:
        failed_test_count += 1
        s += "FAILED ❌❌❌❌❌\n\n\n"
    f.write(s)

def test_is_empty(f) -> None:
    for _ in range(200):
        board = generate_board()
        function = "is_empty"
        args = "board: list"
        print_board(board, f)
        assert_test_result(function, args, is_empty(board), test.is_empty(board), f)

def test_detect_rows(f) -> None:
    for _ in range(1000):
        board = generate_board()
        function = "detect_rows"
        print_board(board, f)
        for col in ['w', 'b']:
            for length in range(2, 9):
                args = f"board: list, '{col}', {length}"
                assert_test_result(function, args, detect_rows(board, col, length), test.detect_rows(board, col, length), f)

def test_search_max(f) -> None:
    for _ in range(200):
        board = generate_board()
        function = "search_max"
        args = "board: list"
        print_board(board, f)
        assert_test_result(function, args, search_max(board), test.search_max(board), f)

def test_is_win(f) -> None:
    for _ in range(2000):
        board = generate_board()
        function = "is_win"
        args = "board: list"
        print_board(board, f)
        assert_test_result(function, args, is_win(board), test.is_win(board), f)

def main() -> None:
    with open("results.txt", "w") as f:
        test_is_empty(f)
        test_detect_rows(f)
        test_search_max(f)
        test_is_win(f)
        f.write(f"{suceeded_test_count}/{suceeded_test_count + failed_test_count} comparisons match")

if __name__ == "__main__":
    main()
