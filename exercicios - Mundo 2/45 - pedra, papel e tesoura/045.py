import random
while True:
    j=(input('Qual você escolhe?\n pedra = 1\n tesoura = 2\n papel = 3\n'))
    c=['pedra','papel','tesoura']
    r= random.choice(c)
    if j==1 and r=='papel':
        print('O computador escolheu: {}'.format(r))
        print('O computador venceu')
    elif j==1 and r=='tesoura':
        print('O computador escolheu: {}'.format(r))
        print('Você venceu')
    elif j==1 and r=='pedra':
        print('O computador escolheu: {}'.format(r))
        print('Empate')
    elif j==2 and r=='pedra':
        print('O computador escolheu: {}'.format(r))
        print('O computador venceu')
    elif j==2 and r=='tesoura':
        print('O computador escolheu: {}'.format(r))
        print('Empate')
    elif j==2 and r=='papel':
        print('O computador escolheu: {}'.format(r))
        print('Você venceu')
    elif j==3 and r=='papel':
        print('O computador escolheu: {}'.format(r))
        print('Empate')
    elif j==3 and r=='pedra':
        print('O computador escolheu: {}'.format(r))
        print('Você venceu')
    elif j==3 and r=='tesoura':
        print('O computador escolheu: {}'.format(r))
        print('O computador venceu')
    else:
        print('Resposta diferente de 1, 2 e 3')

    print('\n\n')
