
cont_m = maior_idade = abaixo_de_20 = escolha = 0
while True:
    idade = int(input('Idade = '))
    sexo = input('sexo [M/F]').upper().strip()
    if sexo not in ['M','F']:
        print('Resposta invalida')
        continue
    escolha = input('Deseja continuar? [s/n]').upper().strip()
    if escolha not in ['S','N']:
        print('Resposta invalida')
        continue
    if idade>=18:
        maior_idade += 1
    if sexo=='M':
        cont_m += 1
    if sexo == 'F' and (idade<20):
           abaixo_de_20 += 1 
    if escolha == 'N':
        break
    
             

    print('\n')

    

print('\n')
print(F'Quantidade de pessoas maior de idade: {maior_idade}')
print(f'Quantidade de homens cadastrados: {cont_m}')
print(f'Tem {abaixo_de_20} mulheres abaixo de 20')   