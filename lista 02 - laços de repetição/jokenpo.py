Nrodadas = int(input())
sheldon = 0
raj = 0

while (Nrodadas > 0):
    escolha_sheldon = input()
    escolha_raj = input()
    Nrodadas = Nrodadas - 1
    if(escolha_sheldon == 'lagarto' and escolha_raj == 'spock'):
        sheldon = sheldon + 1
    elif(escolha_sheldon == 'spock' and escolha_raj == 'lagarto'):
        raj = raj + 1
    elif(escolha_sheldon == 'spock' and escolha_raj == 'tesoura'):
        sheldon = sheldon + 1
    elif(escolha_sheldon == 'tesoura' and escolha_raj == 'spock'):
        raj = raj + 1
    elif(escolha_sheldon == 'tesoura' and escolha_raj == 'lagarto'):
        sheldon = sheldon + 1
    elif(escolha_sheldon == 'lagarto' and escolha_raj == 'tesoura'):
        raj = raj + 1
else:
    if(sheldon > raj):
        print("BAZINGA! EU SOU O SENHOR DA SALA!")
    elif(sheldon < raj):
        print("ENGOLE ESSA, SHELDON!")
    else:
        print("Oh não, precisamos de outra rodada.")