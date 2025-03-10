numero = soma = cont = 0

while True:
    numero = float(input('Digite um numero, (ou 999 para parar):'))
    if numero == 999:
        break
    soma += numero
    cont += 1
print (f'{cont} numeros foram digitados e a soma deles é: {soma}')