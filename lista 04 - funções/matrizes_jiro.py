def soma_matrizes(a,b): #função para somar matrizes
    soma = []
    for i in range(len(a)):
        soma.append([])
        for j in range(len(a[0])):
            soma[i].append(a[i][j] + b[i][j])
    return soma

def diferenca_matrizes(a,b): #função para subtrair matrizes
    diferenca = []
    for i in range(len(a)):
        diferenca.append([])
        for j in range(len(a[0])):
            diferenca[i].append(a[i][j] - b[i][j])
    return diferenca

#dado uma matriz mxn e outra matriz oxp, irá gerar uma matriz mxp
#a multiplicação de matrizes só é possível se n=o
def multiplicacao_matrizes(a,b):
    def linha(matriz, n): #função para definir a linha que irá multiplicar
        return [i for i in matriz[n]] 
    def coluna(matriz, n): #função para definir a coluna que será multiplicada
        return [i[n] for i in matriz]
    mat1linha = len(a) #contabilizar o número de linhas da primeira matriz
    mat2coluna = len(b[0]) #contabilizar o número de colunas da segunda matriz
    multiplicacao = []
    for i in range(mat1linha):
        multiplicacao.append([])
        for j in range(mat2coluna):
            lista_multiplicacao = [x*y for x, y in zip(linha(a, i), coluna(b, j))]
            multiplicacao[i].append(sum(lista_multiplicacao))
    return multiplicacao

def multiplicacao_escalar(a,k): #multiplicando a matriz por k escalar
    multiplicacao = []
    for i in a:
        multiplicacao.append([j * k for j in i])
    return multiplicacao

ordem_matriz = int(input()) #dividindo os inputs 2 matrizes
m1 = []
for i in range(ordem_matriz):
    linha = input().split(' ')
    m1.append([int(j) for j in linha])
m2 = []
for i in range(ordem_matriz):
    linha = input().split(' ')
    m2.append([int(j) for j in linha])

qtd_operacoes = int(input()) #separando as operações em uma lista de operações
operacoes = []
for i in range(qtd_operacoes):
    linha = input().split(' ')
    operacoes.append(linha)

resultado = [] #realizando as operações
for operacao in operacoes: #observar se m1 que recebe a operação
    if operacao[0] == 'm1' and '*' not in operacao: 
        ma = None
        if operacao[2] == 'm1':
            ma = m1
        else:
            ma = m2
        mb = None
        if operacao[4] == 'm1':
            mb = m1
        else:
            mb = m2
        if operacao[3] == '+':
            resultado = soma_matrizes(ma, mb)
            m1 = resultado
        elif operacao[3] == '-':
            resultado = diferenca_matrizes(ma, mb)
            m1 = resultado
        elif operacao[3] == '.':
            resultado = multiplicacao_matrizes(ma, mb)
            m1 = resultado
    elif operacao[0] == 'm1' and '*' in operacao:
        m = None
        k = None
        if operacao[2] == 'm1' or operacao[2] == 'm2':
            k = int(operacao[4])
            if operacao[2] == 'm1':
                m = m1
            else:
                m = m2
        else:
            k = int(operacao[2])
            if operacao[4] == 'm1':
                m = m1
            else:
                m = m2
        resultado = multiplicacao_escalar(m, k)
        m1 = resultado

    #repertir o mesmo para quando m2 receber a operação
    elif operacao[0] == 'm2' and '*' not in operacao:
        ma = None
        if operacao[2] == 'm1':
            ma = m1
        else:
            ma = m2
        mb = None
        if operacao[4] == 'm1':
            mb = m1
        else:
            mb = m2
        if operacao[3] == '+':
            resultado = soma_matrizes(ma, mb)
            m2 = resultado
        elif operacao[3] == '-':
            resultado = diferenca_matrizes(ma, mb)
            m2 = resultado
        elif operacao[3] == '.':
            resultado = multiplicacao_matrizes(ma, mb)
            m2 = resultado
    elif operacao[0] == 'm2' and '*' in operacao:
        m = None
        k = None
        if operacao[2] == 'm1' or operacao[2] == 'm2':
            k = int(operacao[4])
            if operacao[2] == 'm1':
                m = m1
            else:
                m = m2
        else:
            k = int(operacao[2])
            if operacao[4] == 'm1':
                m = m1
            else:
                m = m2
        resultado = multiplicacao_escalar(m, k)
        m2 = resultado
#mostrar o resultado da última operação
for i in resultado:
    linha = [str(j) for j in i]
    print(' '.join(linha))