def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    
    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    
    while True:
        print_board(board)
        row = int(input("Enter the row number (1-3): ")) - 1
        col = int(input("Enter the column number (1-3): ")) - 1
        
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = player
        else:
            print("Invalid move. Try again.")
            continue
        
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if all(' ' not in row for row in board):
            print_board(board)
            print("It's a tie!")
            break
        
        player = 'O' if player == 'X' else 'X'

tic_tac_toe()
