#Bobby = {'arma': 'grande espada', 'armadura': 'armadura media'},Diana = {'arma': 'dardo', 'armadura': 'armadura leve'}, 
#Eric = {'arma': 'grande espada', 'armadura': 'armadura pesada'}, Hank = {'arma': 'espada', 'armadura': 'armadura media'},
#Presto = {'arma': 'cajado', 'armadura': 'armadura leve'}, Sheila = {'arma': 'espada', 'armadura': 'armadura leve'},Uni = {'arma': 'chifre', 'armadura': 'armadura leve'}
#armas = {'chifre': 2, 'cajado': 4, 'espada': 6, 'espada grande': 8, 'dardo': 12}
#armaduras = {'armadura pesada': 0, 'armadura media': 1, 'armadura leve': 3}

#personagens com suas armas e armadura, dano de cada arma, dano recebido pela armadura
status_personagem = {'Bobby_arma': 8, 'Bobby_armadura': 1,'Diana_arma': 12, 'Diana_armadura': 3, 'Eric_arma': 8, 'Eric_armadura': 0,
'Hank_arma': 6, 'Hank_armadura': 1, 'Presto_arma': 4, 'Presto_armadura': 3, 'Sheila_arma': 6, 'Sheila_armadura': 3, 
'Uni_arma': 2, 'Uni_armadura': 3}


adversario = input()
hp_adversario = {}  #recebendo o nome do adversário e seus pontos de vida
if adversario == 'Vingador':
    hp_adversario[adversario] = 30
elif adversario == 'Tiamat':
    hp_adversario[adversario] = 20
elif adversario == 'Vingador das Sombras':
    hp_adversario[adversario] = 14
else:
    hp_adversario[adversario] = 9

turnos = int(input())
fim = False

while not fim:
    personagem = input()
    personagem_arma = personagem + '_arma'  #variável para fazer busca no dicionário
    personagem_armadura = personagem + '_armadura'  #variável para fazer busca no dicionário
    if personagem == 'Mestre dos Magos':
        print('Muito obrigado amigo, que nos vejamos novamente um dia')
        fim = True
    else:
        hp_adversario[adversario] = hp_adversario[adversario] - status_personagem[personagem_arma] #atacar o adversário
        turnos = turnos - status_personagem[personagem_armadura] - 1  #receber dano do adversário
        if hp_adversario[adversario] <= 0:
            print(f'{personagem} executou o ultimo golpe em {adversario}, estamos livres!')
            fim = True
        elif hp_adversario[adversario] > 0 and turnos <=0:
            print(f'Oh nao, {adversario} e muito forte, este e o fim!')
            fim = True