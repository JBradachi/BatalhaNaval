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

def geracaoAleatoria(matrix):
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
    return matrix

def geracao(matrix):
    pequenos = mt.ceil(matrix.size/32)
    medios = mt.ceil(matrix.size/64)
    grandes = mt.ceil(matrix.size/64)
    sizeM = matrix.shape[0]
    print(f"voce pode colocar {pequenos} pequenos, {medios} medios e {grandes} grandes")
    i = int(0)
    print("NAVIOS GRANDES:")
    while i < grandes:
        mostraMapaCriacao(matrix)
        x = int(input(f"coordenada X: Digite um numero entre 0 e {sizeM}"))
        y = int(input(f"coordenada Y: Digite um numero entre 0 e {sizeM}"))
        if verificaPossibilidadeX(matrix, x, y, 4, sizeM):
            for p in range(4):
                matrix[x+p][y] = 4
            i += 1
        elif verificaPossibilidadeY(matrix, x, y, 4, sizeM):
            for p in range(4):
                matrix[x][y+p] = 4
            i += 1
        else:
            print("Não foi possível colocar, tente novamente")
    i = int(0)
    print("NAVIOS MEDIOS:")
    while i < medios:
        mostraMapaCriacao(matrix)
        x = int(input(f"coordenada X: Digite um numero entre 0 e {sizeM}"))
        y = int(input(f"coordenada Y: Digite um numero entre 0 e {sizeM}"))
        if verificaPossibilidadeX(matrix, x, y, 3, sizeM):
            for p in range(3):
                matrix[x+p][y] = 3
            i+=1
        elif verificaPossibilidadeY(matrix, x, y, 3,sizeM):
            for p in range(3):
                matrix[x][y+p] = 3
            i+=1
        else:
            print("Não foi possível colocar, tente novamente")
    i = int(0)
    print("NAVIOS PEQUENOS:")
    while i < pequenos:
        mostraMapaCriacao(matrix)
        x = int(input(f"coordenada X: Digite um numero entre 0 e {sizeM}"))
        y = int(input(f"coordenada Y: Digite um numero entre 0 e {sizeM}"))
        if verificaPossibilidadeX(matrix, x, y, 2, sizeM):
            for p in range(2):
                matrix[x+p][y] = 2
            i+=1
        elif verificaPossibilidadeY(matrix, x, y, 2, sizeM):
            for p in range(2):
                matrix[x][y+p] = 2
            i+=1
        else:
            print("Não foi possível colocar, tente novamente")
    return matrix

def condicaoDeTermino(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                return False
    return True

def jogo(matriz1, matriz2, dificuldade):
    aux1 = defineDificuldade(dificuldade)
    aux2 = defineDificuldade(dificuldade)
    while True:
        print("Jogador 1:")
        while True:
            print("1 - ver lado aliado\n2 - ver lado inimigo\n3 - atacar")
            escolha = int(input(">>> "))
            if escolha == 1:
                mostraMapaCriacao(matriz1)
                print()
            elif escolha == 2:
                mostraMapaCriacao(aux2)
                print()
            elif escolha == 3:
                x = int(input("Escolha uma coordenada x para atacar >>> "))
                y = int(input("Escolha uma coordenada y para atacar >>> "))
                if matriz2[x][y] != 0:
                    print("Acertou")
                    aux2[x][y] = 1
                    matriz2[x][y] = 0
                else:
                    print("Errou")
                    aux2[x][y] = 9
                break
            else:
                print("digite um valor valido")
        if condicaoDeTermino(matriz2):
            print("joagdor 1 ganhou")
            break
            
        print("Jogador 2:")
        while True:
            print("1 - ver lado aliado\n2 - ver lado inimigo\n3 - atacar")
            escolha = int(input(">>> "))
            if escolha == 1:
                mostraMapaCriacao(matriz2)
                print()
            elif escolha == 2:
                mostraMapaCriacao(aux1)
                print()
            elif escolha == 3:
                x = int(input("Escolha uma coordenada x para atacar >>> "))
                y = int(input("Escolha uma coordenada y para atacar >>> "))
                if matriz1[x][y] != 0:
                    print("Acertou")
                    aux2[x][y] = 1
                    matriz1[x][y] = 0
                else:
                    print("Errou")
                    aux1[x][y] = 9
                break
            else:
                print("digite um valor valido")
        if condicaoDeTermino(matriz1):
            print("joagdor 2 ganhou")
            break

matriz1 = defineDificuldade("facil")
matriz1 = geracaoAleatoria(matriz1)
matriz2 = defineDificuldade("facil")
matriz2 = geracaoAleatoria(matriz2)

jogo(matriz1, matriz2, "facil")
