n1=int(input('Digite o primeiro numero inteiro:'))
n2=int(input('Digite o segundo numero inteiro:'))

if n1>n2:
    print('O {} é maior que o {}'.format(n1,n2))
elif n2>n1:
    print('O {} é maior que {}'.format(n2,n1))
else:
    print('Os dois são iguais')