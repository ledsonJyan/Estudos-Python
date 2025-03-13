lista = []
lista_par = []
lista_impar = []

while True:
    numeros = int(input('Digite um numero:'))
    lista.append(numeros)
    lista.sort()
    if numeros % 2 == 0:
        lista_par.append(numeros)
        lista_par.sort()
    if numeros % 2 == 1:
        lista_impar.append(numeros)
        lista_impar.sort()
    escolha = input('Quer continuar? [s/n]').upper()
    print('\n')
    if escolha == 'N':
        break
    else:
        if escolha == 'S':
            continue
        if escolha not in '[S/N]':
            continue
    
print(f'A lista digita é: {lista}')
print(f'A lista par é: {lista_par}')
print(f'A lista impar é: {lista_impar}')