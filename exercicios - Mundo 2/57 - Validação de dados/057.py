sexo = 0
while sexo != 'M' and sexo!= 'F':
    sexo = input('Qual o seu sexo?\n').upper().strip()
    print('\n')
    if sexo != 'M' and sexo!= 'F':
        print('Resposta invalida! so pode M ou F\n')
print('Obrigado pela resposta')