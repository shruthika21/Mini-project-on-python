import random

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

def is_board_full(board):
    # Check if the board is full
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_empty_positions(board):
    # Get empty positions on the board
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    # Base cases for recursive minimax function
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth, None
    elif winner == "O":
        return 10 - depth, None
    elif is_board_full(board):
        return 0, None
    
    # Recursive case
    if is_maximizing:
        max_score = float("-inf")
        best_move = None
        for i, j in get_empty_positions(board):
            board[i][j] = "O"
            score, _ = minimax(board, depth + 1, False)
            board[i][j] = " "
            if score > max_score:
                max_score = score
                best_move = (i, j)
        return max_score, best_move
    else:
        min_score = float("inf")
        best_move = None
        for i, j in get_empty_positions(board):
            board[i][j] = "X"
            score, _ = minimax(board, depth + 1, True)
            board[i][j] = " "
            if score < min_score:
                min_score = score
                best_move = (i, j)
        return min_score, best_move

def tic_tac_toe_ai():
    print("Welcome to Tic-Tac-Toe AI!")

    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Main game loop
    player = "X"
    while True:
        print_board(board)
        
        # Check if it's the player's turn or AI's turn
        if player == "X":
            # Player's turn
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            # Check if the move is valid
            if board[row][col] != " ":
                print("That position is already taken. Try again.")
                continue
            else:
                board[row][col] = "X"
        else:
            # AI's turn (minimax algorithm)
            score, (row, col) = minimax(board, 0, True)
            board[row][col] = "O"
        
        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "X":
                print("Player wins!")
            else:
                print("AI wins!")
            break
        
        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch to the other player
        player = "O" if player == "X" else "X"

if _name_ == "_main_":
    tic_tac_toe_ai()
