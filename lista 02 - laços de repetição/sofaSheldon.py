acao = input()
temperatura = 30
fome = True
internet = 0

while(acao != 'parar'):
    if(acao == 'ir para o grad'):
        temperatura = temperatura - 5
        internet = internet + 300
        acao = input()
    elif(acao == 'sair para a rua'):
        temperatura = temperatura + 5
        acao = input()
    elif(acao == 'comer uma quentinha'):
        fome = False
        acao = input()
    elif(acao == 'conectar no wifi'):
        internet = internet + 100
        acao = input()
    else:
        print("Entrada inválida")
        acao = input()
else:
    if(temperatura >= 30):
        print("A temperatura aqui não está agradável")
    if(temperatura <= 25):
        print("Agora sim, está aconchegante")
    if(fome == True):
        print("Meu corpo precisa de comida")
    if(internet < 100):
        print("Essa conexão está horrível")
    if(temperatura <= 25 and fome == False and internet >= 300):
        print("Finalmente um lugar preciso para mim!")