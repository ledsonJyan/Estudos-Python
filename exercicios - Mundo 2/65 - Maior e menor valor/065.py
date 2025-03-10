numero = opçao = media = soma = cont = maior = menor = 0

while True:
    numero = int(input('Digite um número: '))
    opçao = input('Deseja continuar? [S/N] ').upper()
    
  
    if opçao not in ['S', 'N']:
        print('Resposta diferente de S e N. Tente novamente.')
        continue 

    cont += 1
    soma += numero
    media = soma / cont
    
    
    if cont == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    if opçao == 'N':
        break  
print(f'Você digitou {cont} números e a média é: {media:.2f}')
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')