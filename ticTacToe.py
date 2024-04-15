def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, mark):
    """Checks if the specified mark has won the game."""
    # Check rows, columns, and diagonals for the mark
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)) or \
           all(board[j][i] == mark for j in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)) or \
       all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Checks if the board is full (no empty spaces)."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_mark = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {current_mark}'s turn.")
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1

        # Check if the chosen cell is empty
        if board[row][col] == " ":
            board[row][col] = current_mark
        else:
            print("This cell is already occupied. Try again.")
            continue

        print_board(board)

        # Check for a win or draw
        if check_win(board, current_mark):
            print(f"Player {current_mark} wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        # Switch to the other player's turn
        current_mark = "O" if current_mark == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
