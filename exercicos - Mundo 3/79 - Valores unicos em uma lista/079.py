lista = []

while True:
   
    numero = int(input('Digite um numero:'))
    
    if numero in lista:
        print('Esse numero ja foi registrado\n')
    else:
        lista.append(numero)
        print('Numero registrado com sucesso\n')
    escolha = input('Quer continuar?[s/n]').upper()
    
    print('\n')
    
    if escolha == 'N':
        break
    else: 
        if escolha not in '[S/N]':
           print('Resposta invalida, tente novamente\n')
           continue
        if escolha == 'S':
            continue
lista.sort()
print(lista)