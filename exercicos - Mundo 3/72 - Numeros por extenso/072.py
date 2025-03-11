while True:
    extenso = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'desesseis', 'dezesete', 'dezoito', 'dezenove','vinte'
    numero = int(input('Digite um numero entre 0 e 20:'))
    if numero< 0 or numero> 20:
        print('Resposta invalida, tente novamente')
        break
    print(extenso[numero])
