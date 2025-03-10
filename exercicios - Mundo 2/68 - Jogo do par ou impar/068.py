import random 
computador = random.randint (1,10)
soma = cont = 0
while True:
    numero = int(input('Digite um numero entre 1 e 10:'))
    escolha = input('Você quer par ou impar?').upper()
    soma = computador + numero
    if escolha not in ['PAR', 'ÍMPAR', 'IMPAR']: 
        print('Resposta inválida. Responda com "PAR" ou "ÍMPAR".')
        continue
    if soma % 2 == 0 and escolha == 'PAR':
        print('Você venceu')
    elif soma % 2 == 0 and escolha == 'IMPAR':
        print('Você venceu')
    else:
        print('Você perdeu')
        break
    cont +=1
print(f'Você venceu {cont} vezes')