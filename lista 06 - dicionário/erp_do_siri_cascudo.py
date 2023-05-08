precos_unid = {'trigo': 3, 'fermento': 2, 'manteiga': 6, 'ovos': 2, 'batata': 4, 'arroz': 3, 'siri': 8, 'pao': 2, 'tomate': 2, 'alface': 1, 'picles': 3, 'queijo': 5}

cardapio = {'hamburguer de siri': 24, 'pizza de siri': 42, 'siri frito': 15, 'siri a parmegiana': 24}

receitas = {'hamburguer de siri': ('siri', 'pao', 'alface', 'tomate', 'queijo', 'picles'), 'pizza de siri': ('siri', 'trigo', 'fermento', 'ovos', 'queijo'), 'siri frito': ('siri', 'manteiga'), 'siri a parmegiana': ('siri', 'trigo', 'ovos', 'queijo', 'tomate')}

estoque = {'trigo': 5, 'fermento': 5, 'manteiga': 5, 'ovos': 5, 'batata': 5, 'arroz': 5, 'siri': 5, 'pao': 5, 'tomate': 5, 'alface': 5, 'picles': 5, 'queijo': 5}

caixa = 40 #valor inicial do caixa

clientes = True
demanda = {} #dicionario criado para anotar novos pedidos
qtd_vendida = {} #dicionario criado para contar a quantidade de pedidos vendidos
while clientes:
    try:
        pedido = input()
        if pedido not in cardapio: #caso o pedido não esteja no cardápio
            if pedido not in demanda:
                demanda[pedido] = 1 #adicionando pedido pela primeira vez na demanada
            else:
                demanda[pedido] += 1 #somando o novo pedido na demanda
            if demanda[pedido] < 3: #novo pedido ainda não está disponível
                print(f'{pedido} ainda não é uma opção disponível.')
            else: #adicionando novo pedido
                receita = input().split(' ')
                receita = tuple(receita) #recebendo sua receita
                receitas[pedido] = receita #adicionando a receita do pedido
                preco = 5
                for item in receita: #calculando preço do pedido
                    preco = preco + precos_unid[item] #somando 5 inicial com o valor de cada ingrediente
                cardapio[pedido] = preco
                print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Siri Cascudo.')
        else: #caso pedido esteja no cardápio
            for item in receitas[pedido]: #conferindo o estoque
                if estoque[item] > 0: 
                    estoque[item] -= 1 #diminuindo 1 unidade ao fazer o pedido, se estoque > 0
                else:
                    estoque[item] += 3 #caso estoque esteja vazio, compra 4 unidades do ingrediente e usa 1 na receita. (4 - 1 = 3)
                    caixa = caixa - 4*precos_unid[item] #descontando valor das unidades compradas
            caixa = caixa + cardapio[pedido] #adicionando valor de venda do pedido ao caixa
            if pedido not in qtd_vendida: 
                qtd_vendida[pedido] = 1 #começando a contagem de vendas do pedido
            else:
                qtd_vendida[pedido] += 1 #aumenta em 1 para cada unidade do pedido vendida
            print(f'{pedido} saindo...')
    except EOFError:
        clientes = False
print('##### Fim do expediente #####')
print(f'O lucro obtido no dia de hoje foi de R${caixa - 40}.')
mais_vendido = max(qtd_vendida, key = qtd_vendida.get) #recebendo o pedido mais vendido
if mais_vendido == 'hamburguer de siri':
    print('O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!')
else:
    print(f'{mais_vendido.capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.')