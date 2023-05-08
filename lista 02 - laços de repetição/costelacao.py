#declaração de variáveis
nEstrelas = int(input())
a = 1
b = a + 1
distanciaTotal = 0
primos = False
divisores = 0
fimPrograma = False
fibonacci = 0
ultimo = 1
penultimo = 1
#encerrar programa caso número de estrelas < 3
if(nEstrelas <= 0):
    print('Isso está quebrado, acho que Howard pode me ajudar.')
    fimPrograma = True
elif(0 < nEstrelas < 3):
    print('Acho que bebi demais, eu juro que tinha mais estrelas!')
    fimPrograma = True

if(fimPrograma == False):
    for i in range(0, nEstrelas):
        star_X = int(input())
        star_Y = int(input())
        if(i == 0):
            star_anteriorX = star_X
            star_anteriorY = star_Y
        else:
            distancia = int(((star_X - star_anteriorX)**2 + (star_Y - star_anteriorY)**2)**(1/2))
            print(f'Distância [star{a} <-> star{b}]: {distancia}')
            #a e b apenas tem função de enumerar as estrelas
            a = a + 1
            b = b + 1
            distanciaTotal = distanciaTotal + distancia
            star_anteriorX = star_X
            star_anteriorY = star_Y
            #fazendo a sequencia de fibonacci
            for i in range(1, 76):
                if(i == 1 or i == 2):
                    nFibonacci = 1
                else:
                    nFibonacci = ultimo + penultimo
                    penultimo = ultimo
                    ultimo = nFibonacci
                #comparando se a distancia pertence a sequencia de fibonacci
                if(nFibonacci == distancia):
                  fibonacci = fibonacci + 1
            #reiniciando a sequencia
            ultimo = 1
            penultimo = 1
    for i in range(1, distanciaTotal + 1):
        if(distanciaTotal % i == 0):
            divisores = divisores + 1
    if(divisores <= 2):
        primos = True
    if(fibonacci == nEstrelas - 1 and primos == False):
        print('Yes! Eu consegui!')
    elif(fibonacci == nEstrelas - 1 and primos == True):
        print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')
    elif(fibonacci == nEstrelas - 2):
        print('Oh, não! Eu quase consegui!')
    elif(fibonacci < nEstrelas - 2 and primos == False):
        print('Eu vou acabar como o Stuart :/')
    elif(fibonacci < nEstrelas - 2 and primos == True):
        print('Pelo menos o programa está funcionando...')

#fibonacci = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55... = Fn + Fn-1
#se numero de divisores <= 2: numero é primo