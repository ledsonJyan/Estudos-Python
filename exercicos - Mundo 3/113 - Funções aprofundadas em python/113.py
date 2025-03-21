import sys

def leiaint():
    while True:
        try:
            entrada = input('Digite um número inteiro: ').strip()
            if entrada == "":
                print("Você não digitou nada! Tente novamente.")
                continue
            return int(entrada)
        except KeyboardInterrupt:
            print('\nUsuário interrompeu a entrada. Saindo...')
            sys.exit(0)  
        except ValueError:
            print('Resposta inválida! Tente novamente.')

def leiafloat():
    while True:
        try:
            entrada = input('Digite um número real: ').strip()
            if entrada == "":
                print("Você não digitou nada! Tente novamente.")
                continue
            return float(entrada)
        except KeyboardInterrupt:
            print('\nUsuário interrompeu a entrada. Saindo...')
            sys.exit(0)  
        except ValueError:
            print('Resposta inválida! Tente novamente.')


ninteiro = leiaint()
nreal = leiafloat()

print(f'Você digitou o número inteiro {ninteiro} e o número real {nreal}')