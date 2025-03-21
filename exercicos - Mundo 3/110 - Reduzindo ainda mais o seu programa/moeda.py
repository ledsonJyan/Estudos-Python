def aumentar(a=0, b=0):
    conta = a +(a * b/ 100)
    return conta if format is False else moeda(conta)

def diminuir(a=0, b=0):
    conta = a - (a * b/100)
    return conta if format is False else moeda(conta)

def dobro(a=0):
    conta = a * 2
    return conta if format is False else moeda(conta)

def metade(a=0):
    conta = a / 2
    return conta if format is False else moeda(conta)

def moeda(a=0, b='R$'):
    return f'{b}{a}'.replace('.',',')

def resumo(numero=0, opçao=0, escolha=0):
    print('-'*40)
    print('MENU')
    print('-'*40)
    opçao = int(input(' [1] Aumentar\n [2] Diminuir\n [3] Dobro\n [4] Metade\n'))
    
    if opçao == 1:
        escolha = int(input('Em quanto % quer aumentar?'))
        print(f'O aumento de {escolha}% de {moeda(numero)} é: {aumentar(numero,escolha)}\n')
    if opçao == 2:
        escolha = int(input('Em quanto % quer diminuir?'))
        print(f'A redução de {escolha}% de {moeda(numero)} é: {diminuir(numero,escolha)}\n')
    if opçao == 3:
        print(f'O dobro de {moeda(numero)} é: {dobro(numero)}\n')
    if opçao == 4:
        print(f'A metade de {moeda(numero)} é: {metade(numero)}\n')
    