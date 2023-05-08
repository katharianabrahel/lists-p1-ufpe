def tradutor(numero):
    letra = ''
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
    if numero == 100:
        letra = ' '
    elif 0 <= numero <= 25:
        letra = alfabeto[numero]
    elif 26 <= numero <= 49:
        letra = alfabeto[numero - 26]
    elif 50 <= numero <= 75:
        letra = alfabeto[numero - 50].upper()
    elif 76 <= numero <= 99:
        letra = alfabeto[numero - 76].upper()
    return letra

numeros = input().split(' ')
traducao = []
traduzir = True
for num in numeros:
    if 0 <= int(num) <= 100:
        traducao.append(tradutor(int(num)))
    else:
        traduzir = False
if traduzir:
    print(''.join(traducao))
else:    
    print('Infelizmente os números nao dizem nada')