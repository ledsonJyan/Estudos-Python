n=input('Digite seu nome completo').strip()
nome=n.split()
nome2= nome[len(nome)-1]
print('O seu primeiro nome é: {}'.format(nome[0]))
print('O seu ultimo nome é: {}'.format(nome2))