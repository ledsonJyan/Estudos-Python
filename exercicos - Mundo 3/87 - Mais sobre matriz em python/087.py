matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_total = 0
soma_da_coluna2 = 0
soma_da_coluna3 = 0
for l in range(0,3):
    for c in range(0,3):
       matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
       soma_total += matriz[l][c]
for l in range(0,3):
    for c in range(0,3):
       print(f'[{matriz[l][c]:^5}]', end = '')
       if c == 1:
            soma_da_coluna2 += matriz[l][c]
       if c == 2:
            soma_da_coluna3 += matriz[l][c]
    print()
print(f'A soma de todos os valores é: {soma_total}')
print(f'A soma da coluna dois é: {soma_da_coluna2}')
print(f'A soma da coluna tres é: {soma_da_coluna3}')