vc=float(input('Qual o valor da casa?'))
s=float(input('Qaul o seu salario?'))
a=int(input('Em quantos anos vai pagar?'))
p=vc/(a*12)
vm=(s*30)/100
print('Para pagar uma casa de {}R$ em {} anos'. format(vc,a))
print('A prestação ficara de: {:.2F}'.format(p))
if p<=vm:
    print('O emprestimo foi um sucesso')
else:
    print('O emprestimo foi negado')