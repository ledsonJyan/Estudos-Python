import random
alunos=['lucas','mateus','joão','vitor']
ordem=random.shuffle(alunos)
print('A ordem é: primeiro aluno {}, segundo aluno {}, terceiro aluno {} e quarto aluno {}'.format(*alunos))