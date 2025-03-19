
def maior(*numero):
    if len(numero) == 0:
        print("Nenhum número foi cadastrado.")
    else:
        cont = 0
        for c in numero:
            cont += 1
        print(f'Foram cadastrados {cont} números')
        print(f'Os numeros são: {numero}')
        print(f'O maior número é: {max(numero)}')
maior(4,7,6,2)
maior(6,5,3)
maior(7,8)
maior(5)
maior('nenhum numero cadastrado')
