import math

# Authors:
# Daniel Busarello, Natália Sens Weise, Victor Fernando Poplade, Vinicius Mueller Landi

# Jogadas possíveis e suas respectivas posições na matriz.
slots = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}

# Quadro inicial (todas as posições vazias)
board = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]

# Inicialização dos jogadores.
player = 'O'
ai = 'X'

# Função responsável por exibir o quadro de jogo.
def show_board(board):
    # Váriavel para enumerar as posições
    j = 1

    # Exibe as posições (1 até 9)
    for _ in range(0, 3):
        for _ in range(0, 3):
            print(j, end=" ")
            j += 1
        print()
    print('')
    # Exibe o quadro (com os símbolos 'X' e 'O')
    for row in board:
        for item in row:
            print(item, end=" ")
        print()

# Verifica se a posição selecionada está vazia
def empty_slot(position):
    pos = slots[position]

    if (board[pos[0]][pos[1]] == ' '):
        return True
    else:
        return False

# Função auxiliar para verificar os vencedores
def check_equals_slots(a, b, c):
    return (a == b and b == c and a != ' ')

# Função para verificar se alguém ganhou o jogo
def check_winner():
    winner = None
    
    # Horizontal
    for i in range(0, 3):
        if (check_equals_slots(board[i][0], board[i][1], board[i][2])):
            winner = board[i][0]

    # Vertical
    for i in range(0, 3):
        if (check_equals_slots(board[0][i], board[1][i], board[2][i])):
            winner = board[0][i]
    
    # Diagonais
    if (check_equals_slots(board[0][0], board[1][1], board[2][2])):
        winner = board[0][0]

    if (check_equals_slots(board[2][0], board[1][1], board[0][2])):
        winner = board[2][0]
    
    # Empate
    openSlots = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == ' '):
                openSlots += 1

    if (winner == None and openSlots == 0): 
        return 'empate'
    else: 
        return winner

# Função responsável por inserir a jogada no quadro
def insert_move(player, position):
    # Verifica se a posição escolhida está vazia
    if (empty_slot(position)):
        pos = slots[position]
        board[pos[0]][pos[1]] = player
        show_board(board)

        result = check_winner()
        if (result is not None):
            if (result == 'empate'):
                print("Empate!")
                ask_for_try_again()
            else:
                print("Vencedor: ", result)
                ask_for_try_again()
            
    # Se a posição estiver ocupada, solicita ao jogador que insira outra jogada
    else:
        print('Jogada inválida!')
        position = int(input('Escolha um número para jogada: '))
        show_board(board)
        insert_move(player, position)
        return

# Função minimax
def minimax(board, isMaximizing):
    # Verifica se alguém ganhou o jogo e retorna a pontuação obtida
    result = check_winner()
    if (result is not None):
        if (result == 'X'):
            return 1
        elif (result == 'O'):
            return -1
    elif (result == 'empate'):
        return 0

    # Caso o algorítmo esteja maximizando a jogada (Max), vez do Algorítmo
    if (isMaximizing):
        best_score = -math.inf

        for index in slots.keys():
            pos = slots[index]
            if (board[pos[0]][pos[1]] == ' '):
                board[pos[0]][pos[1]] = ai
                score = minimax(board, False)
                board[pos[0]][pos[1]] = ' '
                best_score = max(score, best_score)
        return best_score

    # Caso o algorítmo esteja minimizando a jogada (Min), vez do Jogador
    else:
        best_score = math.inf

        for index in slots.keys():
            pos = slots[index]
            if (board[pos[0]][pos[1]] == ' '):
                board[pos[0]][pos[1]] = player
                score = minimax(board, True)
                board[pos[0]][pos[1]] = ' '
                best_score = min(score, best_score)
        return best_score

# Função para escolher a jogada do Jogador
def playerMove():
    position = int(input('Escolha um número para O: '))
    insert_move(player, position)
    return

# Função para escolher a jogada da AI, primeira chamada ao Minimax
def aiMove():
    best_score = -math.inf
    best_move = 0

    # Inicia maximizando a jogada
    for index in slots.keys():
        pos = slots[index]
        if (board[pos[0]][pos[1]] == ' '):
            board[pos[0]][pos[1]] = ai
            score = minimax(board, False)
            board[pos[0]][pos[1]] = ' '

            if (score > best_score):
                best_score = score
                best_move = index

    insert_move(ai, best_move)
    return

def ask_for_try_again():
    tryAgain = input("Deseja jogar novamente?(S/N) ")
    if tryAgain == "S" or tryAgain == 's':
        print('----------------------------')
        print('---------NOVO JOGO----------')
        print('')
        restart(board)
        try_again()
    else:
        exit()

def restart(board):
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = ' '

def try_again():
    while not check_winner():
        aiMove()
        playerMove()

# Loop até alguém vencer / empatar o jogo
while not check_winner():
    aiMove()
    playerMove()