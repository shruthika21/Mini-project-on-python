import random

def initialize_board(rows, cols, mines):
    # Create an empty board
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    # Add mines to the board
    for _ in range(mines):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while board[row][col] == -1:
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        board[row][col] = -1
    
    # Calculate adjacent mine counts
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == -1:
                continue
            count = 0
            for x in range(max(0, i - 1), min(rows, i + 2)):
                for y in range(max(0, j - 1), min(cols, j + 2)):
                    if board[x][y] == -1:
                        count += 1
            board[i][j] = count
    
    return board

def print_board(board, reveal=False):
    for row in board:
        for cell in row:
            if cell == -1 and reveal:
                print("*", end=" ")
            elif cell == -1 and not reveal:
                print(".", end=" ")
            else:
                print(cell, end=" ")
        print()

def reveal_cell(board, revealed, row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True
    if board[row][col] == 0:
        for x in range(max(0, row - 1), min(len(board), row + 2)):
            for y in range(max(0, col - 1), min(len(board[0]), col + 2)):
                reveal_cell(board, revealed, x, y)

def play_minesweeper(rows, cols, mines):
    board = initialize_board(rows, cols, mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    game_over = False
    
    while not game_over:
        print_board(revealed)
        
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        
        if board[row][col] == -1:
            print("Game Over! You hit a mine.")
            print_board(board, reveal=True)
            game_over = True
        else:
            reveal_cell(board, revealed, row, col)
            if all(all(revealed[row][col] or board[row][col] == -1 for col in range(cols)) for row in range(rows)):
                print("Congratulations! You win!")
                print_board(board, reveal=True)
                game_over = True

if _name_ == "_main_":
    rows = 5
    cols = 5
    mines = 5
    play_minesweeper(rows, cols, mines)
