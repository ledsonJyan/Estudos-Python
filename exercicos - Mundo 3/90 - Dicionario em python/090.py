dados = dict()
nome = input('Nome do aluno:')
media = float(input('Media do aluno:'))
dados['nome'] = nome
dados['media'] = media

if media >= 70:
    dados['situaçao'] = 'Aprovado'
else:
    dados['situaçao'] = 'Reprovado'

print(f'O nome do aluno(a) é: {dados["nome"]}')
print(f'A media do aluno(a) é: {dados["media"]}')
print(f'A situação do aluno é: {dados["situaçao"]}')