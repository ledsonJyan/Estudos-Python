produto = valor = escolha = soma = cont = menor = 0
barato = ''
while True:
    produto = input('Qual o nome do produto?')
    valor = float(input('Qual o valor?'))
    escolha = input('Deseja continuar? [s/n]').upper().strip()
    if escolha not in ['S','N']:
        print('Resposta invalida')
        continue
    soma += valor
    if valor>1000:
      cont += 1
    
    if menor == 0 or valor < menor:  
        menor = valor
        barato = produto
    if escolha == 'N':
        break

print(f'O total ficou: {soma}')
print(f'Tem {cont} produtos acima de 1000')
print(f'O produto mais barato é: {barato} e vale: {menor}')
