nome_da_quadrilha = input()
passo_1 = input()
passo_2 = input()
passo_3 = input()
passo_4 = input()
passo_5 = input()

pontuacao = 0

if(passo_1 == 'Cumprimento'):
    pontuacao = pontuacao + 100
elif(passo_1 == 'Balancê'):
    pontuacao = pontuacao + 50
elif(passo_1 == 'Passeio'):
    pontuacao = pontuacao + 70
elif(passo_1 == 'Túnel'):
    pontuacao = pontuacao*0.9
elif(passo_1 == 'Serrote'):
    pontuacao = pontuacao + 100
elif(passo_1 == 'Despedida'):
    pontuacao = pontuacao

if(passo_2 == 'Cumprimento'):
    pontuacao = pontuacao + 10
elif(passo_2 == 'Balancê'):
    pontuacao = pontuacao + 50
elif(passo_2 == 'Passeio'):
    pontuacao = pontuacao + 70
elif(passo_2 == 'Túnel'):
    pontuacao = pontuacao*0.9
elif(passo_2 =='Serrote'):
    pontuacao = pontuacao + 100
elif(passo_2 == 'Despedida'):
    pontuacao = pontuacao

if(passo_3 == 'Cumprimento'):
    pontuacao = pontuacao + 10
elif(passo_3 == 'Balancê'):
    pontuacao = pontuacao + 50
elif(passo_3 == 'Passeio'):
    pontuacao = pontuacao + 70
elif(passo_3 == 'Túnel'):
    pontuacao = pontuacao*0.9
elif(passo_3 == 'Serrote'):
    pontuacao = pontuacao + 100
elif(passo_3 == 'Despedida'):
    pontuacao = pontuacao

if(passo_4 == 'Cumprimento'):
    pontuacao = pontuacao + 10
elif(passo_4 == 'Balancê'):
    pontuacao = pontuacao + 50
elif(passo_4 == 'Passeio'):
    pontuacao = pontuacao + 70
elif(passo_4 == 'Túnel'):
    pontuacao = pontuacao*0.9
elif(passo_4 == 'Serrote'):
    pontuacao = pontuacao + 100
elif(passo_4 == 'Despedida'):
    pontuacao = pontuacao

if(passo_5 == 'Cumprimento'):
    pontuacao = pontuacao + 10
elif(passo_5 == 'Balancê'):
    pontuacao = pontuacao + 50
elif(passo_5 == 'Passeio'):
    pontuacao = pontuacao + 70
elif(passo_5 == 'Túnel'):
    pontuacao = pontuacao*0.9
elif(passo_5 == 'Serrote'):
    pontuacao = pontuacao + 100
elif(passo_5 =='Despedida'):
    pontuacao = pontuacao + 35

if(passo_1 == 'Casamento' or passo_2 == 'Casamento' or passo_3 == 'Casamento' or passo_4 == 'Casamento' or passo_5 == 'Casamento'):
    pontuacao = pontuacao*2

if(passo_1 != 'Cumprimento' and passo_1 != 'Balancê' and passo_1 != 'Passeio' and passo_1 != 'Túnel' and passo_1 != 'Serrote' and passo_1 != 'Casamento' and passo_1 != 'Despedida'):
    pontuacao = 0
elif(passo_2 != 'Cumprimento' and passo_2 != 'Balancê' and passo_2 != 'Passeio' and passo_2 != 'Túnel' and passo_2 != 'Serrote' and passo_2 != 'Casamento' and passo_2 != 'Despedida'):
    pontuacao = 0
elif(passo_3 != 'Cumprimento' and passo_3 != 'Balancê' and passo_3 != 'Passeio' and passo_3 != 'Túnel' and passo_3 != 'Serrote' and passo_3 != 'Casamento' and passo_3 != 'Despedida'):
    pontuacao = 0
elif(passo_4 != 'Cumprimento' and passo_4 != 'Balancê' and passo_4 != 'Passeio' and passo_4 != 'Túnel' and passo_4 != 'Serrote' and passo_4 != 'Casamento' and passo_4 != 'Despedida'):
    pontuacao = 0
elif(passo_5 != 'Cumprimento' and passo_5 != 'Balancê' and passo_5 != 'Passeio' and passo_5 != 'Túnel' and passo_5 != 'Serrote' and passo_5 != 'Casamento' and passo_5 != 'Despedida'):
    pontuacao = 0

if(pontuacao == 0):
    print(f'Poxa, {nome_da_quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')
else:
    print(f'Parabéns, {nome_da_quadrilha}! Bela apresentação. A pontuação foi de {pontuacao:.1f}!')