def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1: X, Player 2: O")
    
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Main game loop
    player = 1
    while True:
        print_board(board)
        
        # Prompt the current player for their move
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))

        # Check if the move is valid
        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue
        
        # Make the move
        if player == 1:
            board[row][col] = "X"
        else:
            board[row][col] = "O"
        
        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check for a draw
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch to the other player
        player = 3 - player

if _name_ == "_main_":
    tic_tac_toe()
