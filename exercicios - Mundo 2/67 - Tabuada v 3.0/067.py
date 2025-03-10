escolha = 0
while True:
    escolha = int(input('Qual tabuada você quer?')) 
    if escolha < 0 :
        break
    for c in range (1,11):
      resposta = escolha * c
      print(f'{escolha} x {c} = {resposta}')
print('ACABOU')