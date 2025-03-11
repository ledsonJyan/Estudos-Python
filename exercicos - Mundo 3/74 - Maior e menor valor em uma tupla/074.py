import random

n = (random.randint(1,10), random.randint(1,10), random.randint(1,10),
random.randint(1,10), random.randint(1,10))

print(f'Você sorteou o valor {n}')
print(f'O maior valor é: {max(n)}')
print(f'O menor valor é: {min(n)}')