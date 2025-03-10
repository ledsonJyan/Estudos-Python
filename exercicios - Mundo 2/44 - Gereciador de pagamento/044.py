v=float(input('Qual o valor do produto?'))
p=float(input('Qual a forma de pagamento?\n Em dinheiro = 1\n A vista no cartão = 2 \n 2X no cartão= 3 \n 3x no cartão = 4\n'))
if p==1:
    np= (v*10)/100
    print('Valor a pagar: {}'.format(v - np))
elif p==2:
    pn=(v*5)/100
    print('Valor a pagar: {}'.format(v - pn))
elif p==3:
   pa= v/2
   print('Valor a pagar: {}\n Com duas parcelas de {}'.format(v,pa))
elif p==4:
    m= (v*(1 + 0.20)**3)/3
    print('Parcelas ficaram: {:.2f}'.format(m))

