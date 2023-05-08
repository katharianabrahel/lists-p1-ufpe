fimEstrada = False
jornada = 0
avanco = False

while(not fimEstrada):
    mensagem = input()
    if(mensagem == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or mensagem == 'Leonard seu anão covarde' or mensagem == 'Tu é muito burro Raj'):
        print('Não xingue seus amigos Sheldon!')
        avanco = False
    if(jornada == 0 and mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Que potencial desperdiçado...')
        fimEstrada = True
    elif(jornada == 0 and mensagem == 'Começou a Trabalhar na Caltech'):
        jornada = jornada + 1
        avanco = True

    elif(jornada == 1 and mensagem == 'Bazinga' and avanco == True):
        jornada = jornada - 1
        avanco = False
    elif(jornada == 1 and mensagem == 'Bazinga' and avanco == False):
        jornada = jornada
        avanco = False
    elif(jornada == 1 and mensagem == 'Trabalho sobre a String Theory'):
        jornada = jornada + 1
        avanco = True
    elif(jornada == 1 and mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Tão perto, mas tão longe')
        fimEstrada = True

    elif(jornada == 2 and mensagem == 'Bazinga' and avanco == True):
        jornada = jornada - 1
        avanco = False
    elif(jornada == 2 and mensagem == 'Bazinga' and avanco == False):
        jornada = jornada
        avanco = False
    elif(jornada == 2 and mensagem == 'Ganhar o Chancellor de ciência'):
        jornada = jornada + 1
        avanco = True
    elif(jornada == 2 and mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Tão perto, mas tão longe')
        fimEstrada = True

    elif(jornada == 3 and mensagem == 'Bazinga' and avanco == True):
        jornada = jornada - 1
        avanco = False
    elif(jornada == 3 and mensagem == 'Bazinga' and avanco == False):
        jornada = jornada
        avanco = False
    elif(jornada == 3 and mensagem == 'Pensar na Teoria de Cooper-Hofstader'):
        jornada = jornada + 1
        avanco = False
    elif(jornada == 3 and mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Não desista Sheldon, você ainda têm muito para alcançar!')
        fimEstrada = True

    elif(jornada == 4 and mensagem == 'Bazinga' and avanco == True):
        jornada = jornada - 1
        avanco = False
    elif(jornada == 4 and mensagem == 'Bazinga' and avanco == False):
        jornada = jornada
        avanco = False
    elif(jornada == 4 and mensagem == 'Criou a Super Assimetria'):
        jornada = jornada + 1
        avanco = False
    elif(jornada == 4 and mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Não desista Sheldon, você ainda têm muito para alcançar!')
        fimEstrada = True

    elif(jornada == 5 and mensagem == 'Bazinga' and avanco == True):
        jornada = jornada - 1
        avanco = False
    elif(jornada == 5 and mensagem == 'Ganhar o Nobel'):
        print('Você conseguiu Sheldon, o Nobel é seu!!!')
        fimEstrada = True
    elif(jornada == 5 and mensagem == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Nãoooooo, esse momento ia ser seu Sheldon')
        fimEstrada = True