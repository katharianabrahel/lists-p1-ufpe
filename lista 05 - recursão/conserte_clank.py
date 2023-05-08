def comp_paranteses(frase, n, contagem):
    if n == len(frase): #caso base para encerrar a recursão
        if contagem == 0:
            print('Essa sentença está com os parênteses balanceados, HOORAY!')
        elif contagem >= 0:
            print('A quantidade de parênteses \'(\' está maior que a de \')\', vamos descartá-la')
        else:
            print('A quantidade de parênteses \')\' está maior que a de \'(\', vamos descartá-la')
    else:
        if frase[n] == '(':
            contagem += 1
        elif frase[n] == ')':
            contagem -= 1
        comp_paranteses(frase, n + 1, contagem) #recursão para comparar do primeiro elemento ao último

def contador(frase):
    contagem = 0
    n = 0 #indice do primeiro elemento da setenca
    comp_paranteses(frase, n, contagem)

n_sentencas = int(input())
for i in range (n_sentencas):
    sentenca = input()
    contagem = contador(sentenca)