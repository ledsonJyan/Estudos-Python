pesado = list()
leve = list()
cont = 0

while True:
    nomes = input('Nome = ')
    peso = float(input('Peso = '))
    
    cont += 1
    escolha = input('Quer continuar?[s/n]: ').upper()

    if peso > 70.00:
        pesado.append((nomes, peso))  
    else:
        leve.append((nomes, peso))  

    
    if escolha == 'N':
        break
    elif escolha == 'S':
        pass
    else:
        print('Resposta inválida, tente novamente.')
        continue


print(f'Número de pessoas cadastradas: {cont}')
print(f'Lista de pessoas pesadas: {pesado}')
print(f'Lista de pessoas leves: {leve}')