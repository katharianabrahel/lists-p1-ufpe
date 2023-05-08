qtd_pedras = int(input())
dists1 = input().split(' ')
dists2 = input().split(' ')

dic_dists1 = {}

for i in range (qtd_pedras):
    dic_dists1[i] = dists1[i]
for i in dic_dists1.values():
    if i in dists2:
        dists2.remove(i)
    
if len(dists2) == 0:
    print('Dale Gohan!')
else:
    print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')