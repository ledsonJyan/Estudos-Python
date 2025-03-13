lista = []

for c in range(0,5):
    numero = int(input('Digite um numero:'))
    
    if len(lista) == 0 or numero >= lista[-1]:
        lista.append(numero)
    else:
        for i in range(len(lista)):
            if numero < lista[i]:
                lista.insert(i,numero)
print(lista)
