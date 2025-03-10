s=float(input('Digite o seu salario:'))
if s<=1250:
    ns= (s*15/100) + s
    print('O seu novo salario é: {}'.format(ns))
else:
    ns= (s*10/100) + s
    print('O seu novo salario é: {}'.format(ns))
