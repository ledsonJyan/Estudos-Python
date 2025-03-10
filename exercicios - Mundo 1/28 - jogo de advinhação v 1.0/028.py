import random
print("Eu vou pensar em um numero inteiro de 1 a 5 e você so tem uma chance de acertar qual numero eu pensei")
p=int(input('Qual numero estou pensando?'))
n=random.choice([1,2,3,4,5])
if p==n:
    print('Parabens! você me venceu')
else:
    print('Você perdeu! mais sorte na proxima vez')
print('Esse foi o numero que pensei:',n)
