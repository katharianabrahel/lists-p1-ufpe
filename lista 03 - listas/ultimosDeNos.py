quantidade_mochila = int(input())
nomes = input()
lista_nomes = nomes.split(' ')
espaco_mochila = []
mochilas = []
for i in range (0, quantidade_mochila): #recebendo o tamanho da mochila e adicionando os itens iniciais
    tamanho_mochila = int(input())
    espaco_mochila.append(tamanho_mochila)
    mochilas.append([lista_nomes[i], espaco_mochila[i], 'Lanterna', 'Omega 3 da top therm'])
quantidade_itens = int(input())
for i in range (0, quantidade_itens): #colocando novos itens na mochila
    nome_item = input()
    indice_item = int(input())
    if len(mochilas[indice_item]) - 2 < mochilas[indice_item][1]: # "-2" por conta do espaço preenchido na lista pelo nome e pelo tamanho da mochila
        mochilas[indice_item].append(nome_item)
    else:
        print('Mochila cheia. Não vai dar para levar.')
fim = False
while not fim: #trajetória até o CIN
    acao = input()
    if(acao == 'Tirar da mochila'):
        item_acao = input()
        mochila_acao = int(input())
        if(item_acao in mochilas[mochila_acao]):
            mochilas[mochila_acao].remove(item_acao)
            print(f'{item_acao} usado com sucesso da mochila {mochila_acao}.')
        else:
            print(f'Você não tem {item_acao} na mochila {mochila_acao}.')
    elif(acao == 'Guardar na mochila'):
        item_acao = input()
        mochila_acao = int(input())
        if(len(mochilas[mochila_acao]) - 2 < mochilas[mochila_acao][1]):
            mochilas[mochila_acao].append(item_acao)
            print(f'{item_acao} adicionado na mochila {mochila_acao}.')
        else:
            print(f'Mochila {mochila_acao} cheia!')
    elif(acao == 'CHEGAMOS NO CIN!'):
        fim = True
    else:
        print('Ação inválida.')
for i in range (0, quantidade_mochila):
    print(f'Mochila de {mochilas[i][0]} chegou assim:')
    for j in range (2, len(mochilas[i])):
        print(f'{mochilas[i][j]}')