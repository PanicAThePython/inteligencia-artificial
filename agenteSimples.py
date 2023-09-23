# Natália Sens Weise, BCC, 6sem, IA
import random
import numpy as np
import matplotlib.pyplot as plt

posicaoAgente = []

def geradorSujeira():
    cena = [0, 2]
    for i in range(len(cenario)):
        for j in range(len(cenario)):
            if (cenario[i][j] == 0):
                cenario[i][j] = cena[random.randrange(0, 2)]
                # if cenario[i][j]==2:
                #     posicaoSujeira.append([i, j])
    return cenario

def posicionarAgente(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == 0:
                posicaoAgente.append(i)
                posicaoAgente.append(j)
                return

def printMatriz(matriz):
    for i in matriz:
        print(i)

def getPosicaoAgente():
    return posicaoAgente

def setPosicaoAgente(posicao):
    posicaoAtual = getPosicaoAgente()
    cenario[posicaoAtual[0]][posicaoAtual[1]] = 0
    posicaoAgente[0] = posicao[0]
    posicaoAgente[1] = posicao[1]    

def verificarSujeira(posicao):
    if cenario[posicao[0]][posicao[1]] == 2:
        return 'Sujo'
    else:
        return 'Limpo'

def aspirar(posicao):
    cenario[posicao[0]][posicao[1]] = 0

def andar(posicao):
    movimentos = ['C', 'B', 'E', 'D']
    mova = movimentos[random.randrange(0, 4)]
    if mova == 'C' and (posicao[0] >= 2):
        return setPosicaoAgente([posicao[0] - 1, posicao[1]])
    elif mova == 'B' and (posicao[0] < 4):
        return setPosicaoAgente([posicao[0] + 1, posicao[1]])
    elif mova == 'E' and (posicao[1] >= 2):
        return setPosicaoAgente([posicao[0], posicao[1] - 1])
    elif mova == 'D' and (posicao[1] < 4):
        return setPosicaoAgente([posicao[0], posicao[1] + 1])
    else:
        return andar(posicao)

def acionarAgente(posicao, estado):
    if estado == 'Sujo':
        return aspirar(posicao)
    else:
        andar(posicao)


# Função que exibe o ambiente na tela
def exibir(matriz, posicao):   
    # posicao = getPosicaoAgente()
    
    # Altera o esquema de cores do ambiente
    plt.imshow(matriz, 'gray')
    plt.nipy_spectral() 
    
    # Coloca o agente no ambiente 
    plt.plot([posicao[1]],[posicao[0]], marker='o', color='r', ls='')
    acionarAgente(posicao, verificarSujeira(posicao))

    plt.show(block=False)
    
    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(0.5)    
    plt.clf()


if __name__=="__main__":
    cenario = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
    ]
    geradorSujeira()
    posicionarAgente(cenario)
    posicao = getPosicaoAgente()
    while(True):
        exibir(cenario, posicao)
        # arrumar as cores do gráfico