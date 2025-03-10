t = int(input('Escolha a tabuada de multiplicação que você quer:'))
for c in range(1,11,1):
    resposta = t*c
    print('{} x {}= {}'.format(t,c,resposta))