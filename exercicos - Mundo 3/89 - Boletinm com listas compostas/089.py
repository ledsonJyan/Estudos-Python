lista = [[], []]
while True:
    nome = input('Nome = ')
    nota1 = int(input('Nota 1 = '))
    nota2 = int(input('Nota 2 = '))
    media = (nota1 + nota2)/2
    lista[0].append(nome)
    lista[1].append(media)
    
    continuar = input('Deseja adicionar outro aluno? (s/n): ').lower()
    print('\n')
    if continuar == 'n':
        break
    if continuar == 's':
        continue
    if continuar not in '[s/n]':
        print('Resposta invalida, tente novamente')
        continue
print(f'{"NOME":<30} {"MEDIA":>7}')
print('-'*40)
for c in range(len(lista[0])):  
    print(f'{lista[0][c]:<30} {lista[1][c]:>7.2f}')
