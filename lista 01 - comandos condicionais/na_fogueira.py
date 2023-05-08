nome_1 = input()
pontuacao_1 = int(input())
nome_2 = input()
pontuacao_2 = int(input())
nome_3 = input()
pontuacao_3 = int(input())

if (pontuacao_1 == pontuacao_2 == pontuacao_3):
  if (nome_1 < nome_2 < nome_3):
    print(f'{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}')
  elif (nome_1 < nome_3 < nome_2):
    print(f'{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}')
  elif (nome_2 < nome_1 < nome_3):
    print(f'{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}')
  elif (nome_2 < nome_3 < nome_1):
    print(f'{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}')
  elif (nome_3 < nome_1 < nome_2):
    print(f'{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}')
  elif (nome_3 < nome_2 < nome_1):
    print(f'{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}')

if (pontuacao_1 < pontuacao_2 < pontuacao_3):
  print(f'{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}')
elif (pontuacao_1 < pontuacao_3 < pontuacao_2):
  print(f'{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}')
elif (pontuacao_2 < pontuacao_1 < pontuacao_3):
  print(f'{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}')
elif (pontuacao_2 < pontuacao_3 < pontuacao_1):
  print(f'{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}')
elif (pontuacao_3 < pontuacao_1 < pontuacao_2):
  print(f'{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}')
elif (pontuacao_3 < pontuacao_2 < pontuacao_1):
  print(f'{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}')

if (pontuacao_1 == pontuacao_2 < pontuacao_3): 
  if (nome_1 < nome_2):
    print(f'{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}')
  elif (nome_2 < nome_1):
    print(f'{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}')
elif (pontuacao_1 == pontuacao_2 > pontuacao_3): 
  if (nome_1 < nome_2):
    print(f'{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}')
  elif (nome_2 < nome_1):
    print(f'{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}')
elif (pontuacao_1 == pontuacao_3 < pontuacao_2): 
  if (nome_1 < nome_3):
    print(f'{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}')
  elif (nome_3 < nome_1):
    print(f'{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}')
elif (pontuacao_1 == pontuacao_3 > pontuacao_2): 
  if (nome_1 < nome_3):
    print(f'{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}')
  elif (nome_3 < nome_1):
    print(f'{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}')
elif (pontuacao_2 == pontuacao_3 < pontuacao_1): 
  if (nome_2 < nome_3):
    print(f'{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}\n{nome_1} {pontuacao_1}')
  elif (nome_3 < nome_2):
    print(f'{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}\n{nome_1} {pontuacao_1}')
elif (pontuacao_2 == pontuacao_3 > pontuacao_1): 
  if (nome_2 < nome_3):
    print(f'{nome_1} {pontuacao_1}\n{nome_2} {pontuacao_2}\n{nome_3} {pontuacao_3}')
  elif (nome_3 < nome_2):
    print(f'{nome_1} {pontuacao_1}\n{nome_3} {pontuacao_3}\n{nome_2} {pontuacao_2}')