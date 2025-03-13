lista = []

for c in range(0,5):
    lista.append(float(input(f'Digite um numero qualquer na posição {c}:')))

maior = max(lista)
menor = min(lista)
pos_maior = lista.index(maior)
pos_menor = lista.index(menor)

print('\n')
print(f'Você digitou os numeros {lista}')
print(f'O numero maior é: {maior:.2f}\nNa posição: {pos_maior}\nO menor numero é: {menor:.2f}\nNa posição: {pos_menor}')