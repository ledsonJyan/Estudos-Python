import random
import time
import operator
jogo = {'jogador 1': random.randint(1,6),
'jogador 2': random.randint(1,6),
'jogador 3': random.randint(1,6),
'jogador 4': random.randint(1,6)}

ranking = dict()

for k,v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    time.sleep(1)
ranking =  sorted(jogo.items(), key = operator.itemgetter(1), reverse=True)
print('-='*40)
print('Ranking dos jogadores')
print('-='*40)
for i,b in enumerate(ranking):
    print(f'{i + 1} lugar: {b[0]} com {b[1]}')
    time.sleep(1)