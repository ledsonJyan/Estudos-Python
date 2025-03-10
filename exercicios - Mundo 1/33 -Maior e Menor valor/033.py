v1=int(input('Digite o primeiro valor inteiro:'))
v2=int(input('Digite o segundo valor inteiro:'))
v3=int(input('Digite o terceiro valor inteiro:'))
if v1>v2 and v1>v3:
    print('O {} é o maior'.format(v1))
elif v2>v1 and v2>v3:
    print('O {} é o maior'.format(v2))
else:
    print('O {} é o maior'.format(v3))
if v1<v2 and v3:
     print('O {} é o menor'.format(v1))
elif v2<v3 and v1:
    print('O {} é o menor'.format(v2))
else:
    print('O {} é o menor'.format(v3))
