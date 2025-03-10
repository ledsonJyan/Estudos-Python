produto = valor = escolha = soma = cont = 0
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
    if escolha == 'N':
        break
print(f'O total ficou: {soma}')
print(f'Tem {cont} produtos acima de 1000')
