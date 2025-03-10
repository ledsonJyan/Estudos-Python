from datetime import datetime
p1 = int(input('O ano que a primeira pessoa nasceu:'))
p2 = int(input('O ano que a segunda pessoa nasceu:'))
p3 = int(input('O ano que a terceira pessoa nasceu:'))
p4 = int(input('O ano que a quarta pessoa nasceu:'))
p5 = int(input('O ano que a quinta pessoa nasceu:'))
p6 = int(input('O ano que a sexta pessoa nasceu:'))

cont_maior_de_idade = 0
cont_menor_de_idade = 0
hoje = datetime.now()
ano_de_nascimento = [p1, p2, p3, p4, p5, p6]
for ano in ano_de_nascimento:
    idade = hoje.year - ano
    if idade>= 21:
        
        cont_maior_de_idade += 1
        
    else:
        cont_menor_de_idade +=1

print('Tem {} pessoas maior de idade'.format(cont_maior_de_idade))
print('Tem {} pessoas menor de idade'.format(cont_menor_de_idade))