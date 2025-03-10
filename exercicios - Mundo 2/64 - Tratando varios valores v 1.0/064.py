soma = -999
numero = 0
quantidade = -1

while numero != 999:
    numero = float(input('DIgite um numero inteiro, (para parar digite 999):'))
    soma += numero
    quantidade += 1
    
print('Foram digitados {} numeros e a soma entrte eles é: {}'.format(quantidade,soma))