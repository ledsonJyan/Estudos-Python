def calculaarea():
    base = float(input('Qual a base da area?'))
    altura = float(input('Qual a altura da area?'))
    area = base * altura
    print(f'A sua area é de {area} metros quadrados')
def linha():
    print('-'*40)
linha()
print('PROGRAMA PARA CALCULAR AREA')
linha()
calculaarea()