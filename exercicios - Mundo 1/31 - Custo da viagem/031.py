n=float(input('A viagem é de quantos km?'))
if n<=200:
    v= n*0.50
    print("O valor da passagem é de: {:.2f}".format(v))
else:
    v2= n*0.45
    print('O valor da passagem é de: {:.2f}'.format(v2))