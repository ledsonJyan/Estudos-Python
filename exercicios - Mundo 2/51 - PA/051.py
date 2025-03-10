print('Essa é uma PA ate o numero 100')
primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))

for c in range (primeiro,101,razao):
    print(c, end = '-') 
print('ACABOU')