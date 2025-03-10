print('Escolha a PA que quiser e veja os 10 primeiros termos')
primeiro = int(input('Primeiro termo:'))
razao = int(input('Escolha a razao:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end = '')
    termo += razao 
    cont += 1

print ('FIM')
    