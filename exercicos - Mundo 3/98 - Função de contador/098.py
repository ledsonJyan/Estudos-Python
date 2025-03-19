
import time
def contador(inicio, fim, passo):
    if passo > 0:
        for c in range(inicio, fim + 1, passo):
            print(c, end =', ', flush=True)
            time.sleep(1)
        print('Fim')
    if passo < 0:
        for c in range(inicio, fim - 1, passo):
            print(c,end =', ', flush=True)
            time.sleep(1)
        print('Fim')
def linha():
    print('-'*40)
print('Contando de 1 ate 10')
contador(1,10,1)
print()
time.sleep(2)
print('Contando de 10 ate 1')
contador(10,1,-1)
linha()
print('Agora personalize a sua contagem')
linha()
começo = int(input('De onde vai começar?'))
final = int(input('Onde vai terminar?'))
pulo = int(input('Pulando de quanto em quanto?'))
if pulo < 0:
    if começo < final:
        começo, final = final, começo 
if pulo == 0:
    pulo = 1
linha()
print(f'Contagem de {começo} ate {final} de {pulo} em {pulo}')
linha()
contador(começo,final,pulo)
