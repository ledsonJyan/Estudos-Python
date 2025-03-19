import random
lista = []
def sortear():
    for c in range(5):  
        lista.append(random.randint(1, 10))
    print(f'Os numeros sorteados são:{lista}')
def somapar():
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'A soma dos numeros pares de {lista} são: {soma}')
sortear()
somapar()