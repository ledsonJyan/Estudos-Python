lista = list()
dados = dict()
cont = 0
media = 0
quantidade = 0
mulheres = []

while True:
    dados['nome'] = input('Nome: ')
    cont += 1
    while True:
        dados['sexo'] = input('Sexo[M/F]: ').upper()
        
        if dados['sexo'] not in '[M,F]': 
                print('Resposta invalida!, tente novamente')
                continue
        else:
            break
    dados['idade'] = int(input('Idade: '))
    quantidade += 1
    media += dados['idade']
    media /= quantidade
    lista.append(dados.copy())
    
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    while True:
        escolha = input('Quer continuar?[S/N]').upper()
        if escolha not in '[S/N]':
            print('Resposta invalida!, tente novamente')
            continue  
        
        if escolha == 'S' or escolha == 'N':
               break
    if escolha == 'N':
                break
    

print(lista)
print(f'Você cadastrou {cont} pessoas')
print(f'A media das idades é: {media:.2f}')
print(f'As mulheres cadastradas foram: {",".join(mulheres)}')
print('Pessoas acima da media')
for pessoa in lista:
    if pessoa['idade'] > media:
        print(f"{pessoa['nome']} - {pessoa['sexo']} - {pessoa['idade']} anos")