dia = int(input())

if(17 <= dia <= 26):
  if(dia == 20):
    print("Você escolheu um dia que não irá acontecer nenhum show, tente novamente!")
  elif(dia % 2 == 0):
    print("Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!")
  elif(dia % 2 == 1):
    print("Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!")
else:
  print("Você escolheu um dia que não irá acontecer nenhum show, tente novamente!")