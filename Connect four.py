def print_board(board):
    for row in board:
        print(' '.join(row))

def check_win(board, player):
    # Verificar linhas
    for row in board:
        for i in range(3):
            if row[i] == row[i + 1] == row[i + 2] == row[i + 3] == player:
                return True

    # Verificar colunas
    for i in range(7):
        for j in range(3):
            if board[j][i] == board[j + 1][i] == board[j + 2][i] == board[j + 3][i] == player:
                return True

    # Verificar diagonais \
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == player:
                return True

    # Verificar diagonais /
    for i in range(3):
        for j in range(3, 7):
            if board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3] == player:
                return True

    return False

def connect_four():
    board = [['-' for _ in range(7)] for _ in range(6)]
    players = ['1', '2']
    player_index = 0

    while True:
        print_board(board)
        column = int(input(f'Player {players[player_index]}, escolha a coluna: '))

        for i in range(5, -1, -1):
            if board[i][column] == '-':
                board[i][column] = players[player_index]
                break

        if check_win(board, players[player_index]):
            print_board(board)
            print(f'Player {players[player_index]} ganhou!')
            break

        player_index = (player_index + 1) % 2

connect_four()
