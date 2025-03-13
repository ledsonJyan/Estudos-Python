abertos = 0
fechados = 0
expressao = input('Digite uma expressão: ')

for pararentese in expressao:
    if pararentese == '(':
        abertos += 1  
    elif pararentese == ')':
        fechados += 1  

if abertos == fechados:
    print('A expressão é válida')
else:
    print('A expressão é inválida')
        