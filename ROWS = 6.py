ROWS = 6
COLS = 7

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + "   ".join(map(str, range(1, COLS + 1))))
    print(" +" + "---+" * COLS)
    for row in board:
        print(" | " + " | ".join(row) + " |")
        print(" +" + "---+" * COLS)

def drop_piece(board, col, piece):
    for row in reversed(board):
        if row[col] == " ":
            row[col] = piece
            return True
    return False

def is_valid_location(board, col):
    return board[0][col] == " "

def check_winner(board, piece):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    return False

def is_board_full(board):
    return all(cell != " " for cell in board[0])

def connect_four():
    board = create_board()
    game_over = False
    turn = 0

    print("🎮 Welcome to Connect Four!")
    print_board(board)

    while not game_over:
        piece = "X" if turn % 2 == 0 else "O"
        try:
            col = int(input(f"Player {piece}, choose column (1-{COLS}): ")) - 1
            if 0 <= col < COLS and is_valid_location(board, col):
                drop_piece(board, col, piece)
                print_board(board)

                if check_winner(board, piece):
                    print(f"🏆 Player {piece} wins!")
                    game_over = True
                elif is_board_full(board):
                    print("🤝 It's a draw!")
                    game_over = True
                else:
                    turn += 1
            else:
                print("❌ Invalid move! Try again.")
        except ValueError:
            print("❗ Please enter a valid number.")

if __name__ == "__main__":
    connect_four()
