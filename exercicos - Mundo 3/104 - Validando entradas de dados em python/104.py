def leiaint():
    while True:
        n = (input('Digite um numero inteiro:'))
        if n.isdigit():
            return int(n)
        else:
            continue
n = leiaint()
print(f'Você digitou o numero {n}')
