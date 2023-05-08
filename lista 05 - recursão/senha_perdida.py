def fatorial(n): #definir fatorial por recursão
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def fibonacci(n): #definir fibonacci por recursão
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gerador_lista_fatorial(n): #criar lista com fatorial de 0 até o número desejado
    lista = []
    for i in range(n):
        lista.append(fatorial(i))
    return lista

def gerador_lista_fibonacci(n): #criar lista com fibonacci de 0 até o número desejado
    lista = []
    for i in range(n):
        lista.append(fibonacci(i))
    return lista

def somar_lista(lista1, lista2): 
    soma = []
    for i in range(len(lista1)):
        soma.append(lista1[i] + lista2[i])
    return soma

def multiplicar_lista(lista1, lista2):
    multiplicacao = []
    for i in range(len(lista1)):
        multiplicacao.append(lista1[i] * lista2[i])
    return multiplicacao

def mod26(n): #fazer mod26 para quando indice for > 26, assim obtendo a letra do alfabeto correspondente
    if n < 26:
        return n
    else:
        return mod26(n % 26)

def conversao_num_letra(numeros): #converter numeros baseado no indice do alfabeto começando por 0
    conversao = []
    for num in numeros:
        conversao.append(alfabeto[mod26(num)])
    return ''.join(conversao)


alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

senha = input()
n_palavras = int(input())
palavras = []
for i in range(n_palavras): #adicionando as palavras em uma lista
    palavras.append(input())
    
palavras_alteradas = [] #lista com as palavras recebidas, alteradas pela distorção. será usada para comparar com a senha.
for palavra in palavras:
    lista_comparacao = [] #lista para receber as transformações de cada palavra
    for letra in palavra:
        mod11 = alfabeto.index(letra) % 11
        if mod11 != 0:
            sequencia_fibonacci = gerador_lista_fibonacci(mod11)
            sequencia_fatorial = gerador_lista_fatorial(mod11)
            if mod11 % 2 != 0:
                sequencia_numeros = multiplicar_lista(sequencia_fibonacci, sequencia_fatorial)
            else:
                sequencia_numeros = somar_lista(sequencia_fibonacci, sequencia_fatorial)
            lista_comparacao.append(conversao_num_letra(sequencia_numeros))
        else:
            lista_comparacao.append('1')
    palavras_alteradas.append(''.join(lista_comparacao)) #juntar as transformações para gerar uma lista com palavras distorcidas

if senha in palavras_alteradas: #checkar se alguma palavra corresponde a senha
    print('Achamos! Achamos a senha.')
else:
    print('É... Temos que procurar mais.')