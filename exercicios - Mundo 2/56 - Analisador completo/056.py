soma_idade = 0
maior = 0
homem_velho = ''
abaixo_de_20 = 0
for c in range (1,5):
    print('-----{}ª PESSOA-----'.format(c))
    nome = input('Nome = ').strip()
    idade = int(input('Idade = '))
    sexo = input('sexo [M/F]').upper().strip()
    soma_idade = soma_idade + idade
    
    if sexo=='M' and (c == 1 or idade>maior):
        maior = idade
        homem_velho = nome
    if sexo == 'F' and (idade<20):
           abaixo_de_20 += 1 
             

    print('\n')

    

media = soma_idade / 4
print('A media da idade é: {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior,homem_velho))
print('Tem {} mulheres abaixo de 20'.format(abaixo_de_20))   


    

