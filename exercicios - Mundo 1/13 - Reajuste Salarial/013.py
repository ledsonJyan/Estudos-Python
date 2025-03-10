s=float(input('Coloque o seu salario:'))
d=float(input('Coloque a porcetagem de aumento:'))
c=s*(d/100)
ns=s+c
print('O novo salario com o aumento é: {:.2f}'.format(ns))