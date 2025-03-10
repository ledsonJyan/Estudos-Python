d = int(input('Quantos por dias foi alugado?'))
k = float(input('Quantos km rodados?'))
t = (d * 60) + (k * 0.15)
print('O valor total a ser pago é: {:.2f}'.format(t))