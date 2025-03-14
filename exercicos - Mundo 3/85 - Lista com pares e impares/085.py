lista = [[], []]

for c in range(0,7):
    numero = int(input('Digite um numero:'))
    if numero % 2 == 0:
        lista[0].append(numero)
        lista[0].sort()
    if numero % 2 == 1:
        lista[1].append(numero)
        lista[1].sort()

print(lista)