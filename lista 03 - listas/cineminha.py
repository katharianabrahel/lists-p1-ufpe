nome = input()
quantidade = int(input())
lista_filme = []
lista_nota = []
decrescente = False
#recebe o nome e a nota do filme, seperando-os em listas
for i in range(quantidade):
    nome_nota_filme = input()
    lista_nome_nota = nome_nota_filme.split(' - ')
    lista_filme.append(lista_nome_nota[0])
    lista_nota.append(lista_nome_nota[-1])
#bubble sort
for j in range(quantidade):
    for i in range(0, quantidade - 1):
        if(lista_nota[i] < lista_nota[i + 1]):
            mudança_nota = lista_nota[i]
            lista_nota[i] = lista_nota[i + 1]
            lista_nota[i + 1] = mudança_nota
            mudança_filme = lista_filme[i]
            lista_filme[i] = lista_filme[i + 1]
            lista_filme[i + 1] = mudança_filme
if(nome == 'João'):
    print('Os filmes sugeridos por João são:')
    for i in range(quantidade):
        print(f'{lista_filme[i]} - {lista_nota[i]}')
elif(nome == 'Bonna'):
    print('Os filmes sugeridos por Bonna são:')
    for i in range(quantidade):
        print(f'{lista_filme[i]} - {lista_nota[i]}')