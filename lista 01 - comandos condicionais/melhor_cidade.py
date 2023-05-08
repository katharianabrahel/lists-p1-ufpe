cidade1 = input()
nota1 = float(input())
distancia1 = int(input())
cidade2 = input()
nota2 = float(input())
distancia2 = int(input())
cidade3 = input()
nota3 = float(input())
distancia3 = int(input())

if(nota1 < 4 and nota2 < 4 and nota3 < 4):
    print("Nota mínima não atingida")
else:
    if(nota1 > nota2 >= nota3):
        print(cidade1)
    elif(nota1 > nota3 >= nota2):
        print(cidade1)
    elif(nota2 > nota1 >= nota3):
        print(cidade2)
    elif(nota2 > nota3 >= nota1):
        print(cidade2)
    elif(nota3 > nota2 >= nota1):
        print(cidade3)
    elif(nota3 > nota1 >= nota2):
        print(cidade3)
    elif(nota1 == nota2 > nota3 and distancia1 < distancia2):
        print(cidade1)
    elif(nota1 == nota2 > nota3 and distancia2 < distancia1):
        print(cidade2)
    elif(nota1 == nota3 > nota2 and distancia1 < distancia3):
        print(cidade1)
    elif(nota1 == nota3 > nota2 and distancia3 < distancia1):
        print(cidade3)
    elif(nota2 == nota3 > nota1 and distancia2 < distancia3):
        print(cidade2)
    elif(nota2 == nota3 > nota1 and distancia3 < distancia2):
        print(cidade3)
    elif(nota1 == nota2 == nota3 and distancia1 < distancia2 <= distancia3):
        print(cidade1)
    elif(nota1 == nota2 == nota3 and distancia1 < distancia3 <= distancia2):
        print(cidade1)
    elif(nota1 == nota2 == nota3 and distancia2 < distancia1 <= distancia3):
        print(cidade2)
    elif(nota1 == nota2 == nota3 and distancia2 < distancia3 <= distancia1):
        print(cidade2)
    elif(nota1 == nota2 == nota3 and distancia3 < distancia1 <= distancia2):
        print(cidade3)
    elif(nota1 == nota2 == nota3 and distancia3 < distancia2 <= distancia1):
        print(cidade3)