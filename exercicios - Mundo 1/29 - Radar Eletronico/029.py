v=float(input('Qual a sua velocidade?'))
if v>60:
    m=(v-80)*7
    print('Voce foi multado, o valor da multa é de: {}'.format(m))
else:
    print('Você ta dentro do limite de velocidade')
