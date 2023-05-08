def separador_silaba(str): #função para separar sílabas
    vogais = set('aeiou')
    start = 0
    silabas = []
    for i in range(len(str)):
        if palavra[i] in vogais:
            silabas.append(str[start:i + 1])
            start = i + 1
    return silabas

def ordendar_palavra(palavra): #função para checkar se a palavra está em ordem
    ordenado = False
    indice = 0
    ultimo_indice = 0
    contador = 0
    while contador < len(palavra):
        if contador == 0:
            ultimo_indice = nome_hospital.index(palavra[contador])
        else:
            indice = nome_hospital.index(palavra[contador])
            if indice - 1 == ultimo_indice:
                ordenado = True
        contador += 1
    return ordenado

nome_hospital = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']
indice_silaba_lembrada = []
fim = False
while not fim:
    palavra = input()
    lista_silabas = separador_silaba(palavra)
    silaba_nome_hospital = []
    for j in lista_silabas:
        if j in nome_hospital:
            indice_silaba_hospital = nome_hospital.index(j)
            #esse condicional serve para não repetir sílabas
            if indice_silaba_hospital not in indice_silaba_lembrada: 
                indice_silaba_lembrada.append(indice_silaba_hospital)
                silaba_nome_hospital.append(j)

    if len(silaba_nome_hospital) == 1:
        print(f'Lembrei! A sílaba {silaba_nome_hospital[0]} está no nome do hospital. Obrigada, Totoro!')
    elif len(silaba_nome_hospital) >= 2:
        em_ordem = ordendar_palavra(silaba_nome_hospital)
        if em_ordem and ''.join(silaba_nome_hospital) == palavra:
            espaco = ''
            print(f'A palavra {espaco.join(silaba_nome_hospital)} está toda no nome do hospital. Acertou em cheio, Totoro!')
        else:
            separar = ', '
            print(f'Lembrei! As sílabas: {separar.join(silaba_nome_hospital)} estão no nome do hospital. Obrigada, Totoro!')
    else:
        print('Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')
    
    indice_silaba_lembrada.sort()
    if indice_silaba_lembrada == [0, 1, 2, 3, 4, 5]:
        print('Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')
        fim = True