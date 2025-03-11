numeros = (int(input('Digite um numero inteiro:')), int(input('Digite um numero inteiro:')),
int(input('Digite um numero inteiro:')), int(input('Digite um numero inteiro:')))
print(f'o numero 9 aparece {numeros.count(9)} vezes')
   

if 3 in numeros:
    print(f'O numero 3 aparece na posição {numeros.index(3)+1}')
else:
    print('O numero 3 não aparece em nenhuma posição ')

pares = [num for num in numeros if num % 2 == 0]
print(f'Os números pares são: {pares}')