## Código de batalha naval simples ##
import numpy as np
import math as mt
import random as rd
def mostraMapaCriacao(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]} ", end="")
        print()

def defineDificuldade(dificuldade):
    if dificuldade == "medio":
        return np.zeros(shape= (10,10), dtype=int)
    elif dificuldade == "dificil":
        return  np.zeros(shape= (12,12), dtype=int)
    else:
        # dificuldade == "facil":
        return np.zeros(shape= (8,8), dtype=int)

def verificaPossibilidadeX(matrix, x, y, passos, sizeM):
    if (x+passos)>sizeM:
        return False
    for i in range(passos):
        if matrix[x+i][y] != 0:
            return False
    return True

def verificaPossibilidadeY(matrix, x, y, passos, sizeM):
    if (y+passos)>sizeM:
        return False
    for i in range(passos):
        if matrix[x][y+i] != 0:
            return False
    return True 

def geraçãoAleatoria(matrix):
    pequenos = mt.ceil(matrix.size/32)
    medios = mt.ceil(matrix.size/64)
    grandes = mt.ceil(matrix.size/64)
    sizeM = matrix.shape[0]
    
    i = int(0)
    while i < grandes:
        x = rd.randint(0, sizeM-1)
        y = rd.randint(0, sizeM-1)
        if verificaPossibilidadeX(matrix, x, y, 4, sizeM):
            for p in range(4):
                matrix[x+p][y] = 4
            i += 1
        elif verificaPossibilidadeY(matrix, x, y, 4, sizeM):
            for p in range(4):
                matrix[x][y+p] = 4
            i += 1
    i = int(0)
    while i < medios:
        x = rd.randint(0, sizeM-1)
        y = rd.randint(0, sizeM-1)
        if verificaPossibilidadeX(matrix, x, y, 3, sizeM):
            for p in range(3):
                matrix[x+p][y] = 3
            i+=1
        elif verificaPossibilidadeY(matrix, x, y, 3,sizeM):
            for p in range(3):
                matrix[x][y+p] = 3
            i+=1
    i = int(0)
    while i < pequenos:
        x = rd.randint(0, sizeM-1)
        y = rd.randint(0, sizeM-1)
        if verificaPossibilidadeX(matrix, x, y, 2, sizeM):
            for p in range(2):
                matrix[x+p][y] = 2
            i+=1
        elif verificaPossibilidadeY(matrix, x, y, 2, sizeM):
            for p in range(2):
                matrix[x][y+p] = 2
            i+=1
    mostraMapaCriacao(matrix)

matriz = defineDificuldade("facil")
geraçãoAleatoria(matriz)
