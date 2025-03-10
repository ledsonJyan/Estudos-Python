n = input('Digite um numero de 6 digitos:')
pares= 0
for c in n:
    if int (c) %2==0:
       pares += int(c)
print('A soma de todos os numeros pares é: {}'.format(pares))