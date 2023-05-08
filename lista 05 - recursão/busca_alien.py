def busca_binária_recursiva(lista, item, esquerda, direita, contador): #busca binária
    if (esquerda + direita) % 2 == 0: #defindo o meio da lista baseado na qtd de salas
        meio = int((esquerda + direita) / 2)
    else:
        meio = int(((esquerda + direita) + 1) / 2)
    if direita < esquerda: #caso base
        return -1
    elif direita == esquerda: #caso tenha apenas uma sala
        contador.append('Meio')
        return contador
    elif lista[meio] == item: #achou a sala
        contador.append('Meio')
        return contador
    elif lista[meio] > item: #mover para esquerda
        contador.append('Esquerda')
        return busca_binária_recursiva(lista, item, esquerda, meio - 1, contador)
    elif lista[meio] < item: #mover para direita
        contador.append('Direita')
        return busca_binária_recursiva(lista, item, meio + 1, direita, contador)

def conversao_num_binario(n): #transformar em número binário
    quociente = 1
    binario = []    #preferi criar uma lista com os algarismos do número binário para poder acrescentar
                    #'0' caso o núermo de bits seja maior
    while quociente >= 1:
        resto = int(n) % 2
        binario.insert(0, str(resto))
        quociente = int(int(n) / 2)
        n = quociente
    return binario

num_salas = input()
lista_num_salas = num_salas.split(' ') #tranformando os números das salas em uma lista
sala_escolhida = input() 
qtd_bits = int(input())
sala_escolhida_binario = conversao_num_binario(sala_escolhida)

passos = []
if sala_escolhida in lista_num_salas: #dividindo o problema em 2 casos: sala escolhida na lista de salas ou não
    busca_binária_recursiva(lista_num_salas, sala_escolhida, 0, len(lista_num_salas) -1, passos)
    if len(sala_escolhida_binario) == qtd_bits:        
        setinha = ' -> '
        espaco = ''
        print(f'{setinha.join(passos)}, seguindo por essas coordenadas você vai chegar no número {espaco.join(sala_escolhida_binario)}.')
    elif len(sala_escolhida_binario) < qtd_bits:
        while len(sala_escolhida_binario) < qtd_bits: #acrescentando '0' até o número de bits informado
            sala_escolhida_binario.insert(0, '0')
        setinha = ' -> '
        espaco = ''
        print(f'{setinha.join(passos)}, seguindo por essas coordenadas você vai chegar no número {espaco.join(sala_escolhida_binario)}.')
    else:
        print('Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.')
else:
    if int(sala_escolhida) < int(lista_num_salas[0]) or int(sala_escolhida) > int(lista_num_salas[-1]): #sala fora do limite da lista
        print('Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.')
    elif int(sala_escolhida) > int(lista_num_salas[0]) and int(sala_escolhida) < int(lista_num_salas[-1]): #sala dentro do intervalo das salas, mas não está na lista de salas
        if len(sala_escolhida_binario) < qtd_bits: 
            busca_binária_recursiva(lista_num_salas, sala_escolhida, 0, len(lista_num_salas) -1, passos)
            setinha = ' -> '
            print(f'{setinha.join(passos)}, mas não consegui achar.')
        elif len(sala_escolhida_binario) > qtd_bits:
            print('Busquei muito, mas não achei a sala, que nem posso dizer, já que tenho poucos bits.')