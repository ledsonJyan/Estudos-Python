lista = []
cont = 0

while True:
    numero = int(input('Digite um numero:'))
    lista.append(numero)
    cont += 1
    escolha = input('Quer continuar? [s/n]').upper()
    print('\n')
    if escolha == 'N':
        break
    else:
        if escolha == 'S':
            continue
        if escolha not in '[S/N]':
            continue
       

lista.sort(reverse = True)    
print(f'Foram digitados {cont} numeros')
print(lista)
if 5 in lista:
        print('O numero 5 foi digitado e está na lista')
else:
        print('O numero 5 não foi digitado e não esta na lista')