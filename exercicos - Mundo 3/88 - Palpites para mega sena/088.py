import random

escolha = int(input('Quantos numeros você quer sortear?'))
lista = list()

for c in range(0,escolha):
    numeros = random.sample(range(1, 61), 6)
    numeros.sort()
    lista.append(numeros)
    print(f'Jogo {c + 1} = {numeros}')
print('Boa sorte')