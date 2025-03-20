import math
def fatorial(a=0, show=False):
    resultado = math.factorial(resposta)
    if show:
        for c in range(a, 0, -1):
            print(c, end = '', flush=True)
            if c > 1:
                print(' x ', end ='', flush=True)

        print(' = ', end = '', flush=True)
    print(resultado)

resposta = int(input('Qual numero você quer fatorar?'))   
fatorial(resposta)