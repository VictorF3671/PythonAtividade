def tralha(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def verifica(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def velha():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        tralha(board)
        print(f"É a vez do jogador {players[current_player]}")

        row = int(input("Digite o número da linha (0-2): "))
        col = int(input("Digite o número da coluna (0-2): "))

        if board[row][col] != ' ':
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        board[row][col] = players[current_player]

        winner = verifica(board)
        if winner:
            tralha(board)
            print(f"O jogador {winner} venceu!")
            break

        if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
            tralha(board)
            print("Deu velha! O jogo terminou em empate.")
            break

        current_player = (current_player + 1) % 2

velha()