atividade = True
pokedex = {}
while atividade:  #repetir o processo indefinademente
    try:
        comando = input().split(' ')  #separando o input em uma lista
        if 'ADD' in comando:
            pokemon = comando[-1]
            if pokemon not in pokedex: #adicionando o pokemon na pokedex
                print('Pokémon adicionado com sucesso')
            else:
                print('Pokémon já adicionado na Pokédex')
        elif 'DESC' in comando: #mostrar a descrição do pokemon
            pokemon = comando[-1]
            if pokemon in pokedex:
                print(pokedex[pokemon])
            else:
                print('Ainda não há registro desse Pokémon')
        else: #adicionando à pokedex a descrição ao pokemon do comando "ADD" anterior
            pokedex[pokemon] = ' '.join(comando) #pokemon usado na linha 7
    except EOFError:
        #break
        atividade = False