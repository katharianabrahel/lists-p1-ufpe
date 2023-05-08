nome = input()
mapa = []
for i in range (0,8):
    mapa.append(list(input()))

pi = 0
pj = 0
di = 0
dj = 0

fim = False
while not fim:
    #posição inicial
    for linha in mapa:
        if 'p' in linha:
            pi = mapa.index(linha)
            pj = linha.index('p')
        if 'd' in linha:
            di = mapa.index(linha)
            dj = linha.index('d')
    novo_pi = pi
    novo_pj = pj
    novo_di = di
    novo_dj = dj
    
    #mover personagem para direita
    if mapa[pi][pj + 1] == '.' and pj + 1 != novo_pj:
        mapa[pi][pj] = '.'
        mapa[pi][pj + 1] = 'p'
    elif mapa[pi][pj + 1] == 'o':
        mapa[pi][pj] = '.'
        for linha in mapa:
            print(''.join(linha))
            print(f'UFA!!! Você e {nome} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
        fim = True
    #mover personagem para baixo
    elif mapa[pi + 1][pj] == '.' and pi + 1 != novo_pi:
        mapa[pi][pj] = '.'
        mapa[pi + 1][pj] = 'p'
    elif mapa[pi + 1][pj] == 'o':
        mapa[pi][pj] = '.'
        for linha in mapa:
            print(''.join(linha))
            print(f'UFA!!! Você e {nome} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
        fim = True
    #mover personagem para cima
    elif mapa[pi - 1][pj] == '.' and pi - 1 != novo_pi:
        mapa[pi][pj] = '.'
        mapa[pi - 1][pj] = 'p'
    elif mapa[pi - 1][pj] == 'o':
        mapa[pi][pj] = '.'
        for linha in mapa:
            print(''.join(linha))
            print(f'UFA!!! Você e {nome} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
        fim = True
    #mover personagem para esquerda
    elif mapa[pi][pj - 1] == '.' and pj - 1 != novo_pj:
        mapa[pi][pj] = '.'
        mapa[pi][pj - 1] = 'p'
    elif mapa[pi][pj - 1] == 'o':
        mapa[pi][pj] = '.'
        for linha in mapa:
            print(''.join(linha))
            print(f'UFA!!! Você e {nome} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
        fim = True
