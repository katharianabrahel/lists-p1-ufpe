tamanho_matriz = int(input())
matriz = []
linha_int = []
for i in range (0,tamanho_matriz): #recebendo as linhas da matriz
    linha = input().split(' ')
    for j in range (0, tamanho_matriz): #transformando o input em inteiros
        linha_int.append(int(linha[j]))
    matriz.append(linha_int)
    linha_int = []
for i in range (0, tamanho_matriz): #achando a soma e a senha das linhas
    for j in range (0, tamanho_matriz - 1):
        if(i == 0 and j == 0):
            soma_linha = matriz[i][j] + matriz[i][j + 1]
            senha_linha = [matriz[i][j], matriz[i][j + 1]]
        else:
            if(matriz[i][j] + matriz[i][j + 1] > soma_linha):
                soma_linha = matriz[i][j] + matriz[i][j + 1]
                senha_linha = [matriz[i][j], matriz[i][j + 1]]
for j in range (0, tamanho_matriz): #achando a soma e a senha das colunas
    for i in range (0, tamanho_matriz - 1):
        if(i == 0 and j == 0):
            soma_coluna = matriz[i][j] + matriz[i + 1][j]
            senha_coluna = [matriz[i][j], matriz[i + 1][j]]
        else:
            if(matriz[i][j] + matriz[i + 1][j] > soma_coluna):
                soma_coluna = matriz[i][j] + matriz[i + 1][j]
                senha_coluna = [matriz[i][j], matriz[i + 1][j]]
for i in range (0, tamanho_matriz - 1): #achando a soma e a senha da diagonal principal
    for j in range(0, tamanho_matriz -1):
        if(i == j):
            if(i == 0 and j == 0):
                soma_diagonal = matriz[i][j] + matriz[i + 1][j + 1]
                senha_diagonal = [matriz[i][j], matriz[i + 1][j + 1]]
            else:
                if(matriz[i][j] + matriz[i + 1][j + 1] > soma_diagonal):
                    soma_diagonal = matriz[i][j] + matriz[i + 1][j + 1]
                    senha_diagonal = [matriz[i][j], matriz[i + 1][j + 1]]
print('Falei que era fácil Dustinzinho...')
print('Pegando todas os números que formam as combinações dos pares de cada sentido temos...')
print(f'Password: {senha_linha[0]}{senha_linha[1]}{senha_coluna[0]}{senha_coluna[1]}{senha_diagonal[0]}{senha_diagonal[1]}')