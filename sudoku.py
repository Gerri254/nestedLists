import random

def print_board(board):
    """Prints the Sudoku board."""
    for row in board:
        print(" ".join(str(cell) for cell in row))

def generate_sudoku():
    """Generates a new Sudoku puzzle."""
    board = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            board[i][j] = (i * 3 + i // 3 + j) % 9 + 1
    random.shuffle(board)
    for i in range(9):
        random.shuffle(board[i])
    return board

if __name__ == "__main__":
    sudoku_board = generate_sudoku()
    print("Generated Sudoku Puzzle:")
    print_board(sudoku_board)


