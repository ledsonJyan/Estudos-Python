import random
print("Eu vou pensar em um numero inteiro de 1 a 10 e você vai tentar acertar qual numero eu pensei")
n=random.choice([1,2,3,4,5,6,7,8,9,10])
tentativa = 0
p = 0
while p!= n:
    p=int(input('Qual numero estou pensando?'))
    tentativa += 1
    if p>n:
        print('Seu palpite foi alto, tente novamente\n')
    if p<n:
        print('Seu palpite foi baixo, tente novamente\n')
    if p==n:
        print('Parabens! você acertou\n')

print('Esse foi o numero que pensei: {}'.format(n))
print('Você acertou em {} tentativas'.format(tentativa))