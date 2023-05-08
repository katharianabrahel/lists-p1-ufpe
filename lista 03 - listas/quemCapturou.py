nomes = input()
separarNomes = nomes.replace(',', ' ')
listaNomes = separarNomes.split()
quantidadeNomes = len(listaNomes)

while quantidadeNomes > 1:
    relatorio = input()
    if(relatorio == 'Não encontrei nada no primeiro suspeito'):
        listaNomes.pop(0)
        quantidadeNomes -= 1
    elif(relatorio == 'O último da lista está limpo'):
        listaNomes.pop(-1)
        quantidadeNomes -= 1
    elif(relatorio == 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita'):
        if(quantidadeNomes % 2 == 0):
            nomeRemovido = int((quantidadeNomes/2))
            listaNomes.pop(nomeRemovido)
            quantidadeNomes -= 1
        else:
            nomeRemovido = int((quantidadeNomes - 1)/2)
            listaNomes.pop(nomeRemovido)
            quantidadeNomes -= 1
    elif(relatorio == 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:'):
        posicao = int(input())
        listaNomes.pop(posicao)
        quantidadeNomes -= 1
    elif(relatorio == 'Acho que temos mais uma opção a ser analisada…'):
        novoNome = input()
        listaNomes.append(novoNome)
        quantidadeNomes += 1
    else:
        print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')
print(f'Acho que encontramos o suspeito. O seu nome é {listaNomes[0]}, vamos salvar o Sam!')