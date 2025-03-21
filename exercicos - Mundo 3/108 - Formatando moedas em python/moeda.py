def aumentar(a=0, b=0):
    conta = a +(a * b/ 100)
    return conta

def diminuir(a=0, b=0):
    conta = a - (a * b/100)
    return conta

def dobro(a=0):
    conta = a * 2
    return conta

def metade(a=0):
    conta = a / 2
    return conta

def moeda(a=0, b='R$'):
    return f'{b}{a}'.replace('.',',')