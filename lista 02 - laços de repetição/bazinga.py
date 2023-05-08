fimShow = False
gostouPiada = 0
naoGostou = 0

while(not fimShow):
    piada = input()
    if(piada == 'Fim do Show!'):
        fimShow = True
    else:
        reacao = input()
        if(reacao == 'BAZINGA!'):
            gostouPiada = gostouPiada + 1
        else:
            naoGostou = naoGostou + 1
if(gostouPiada > 0.6*(gostouPiada + naoGostou)):
  print("BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!")
elif(naoGostou > 0.6*(gostouPiada + naoGostou)):
  print("Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!")
else:
  print("Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!")