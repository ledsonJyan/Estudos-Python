soma = 0
cont = 0
for c in range (1,501,1):
    if (c % 2==1) and (c % 3==0):
        soma = soma + c
        cont = cont + 1
        print(c)
print('A quantidade de numeros é: {}'.format(cont))
print('A soma de todos os valores é: {}'.format(soma))