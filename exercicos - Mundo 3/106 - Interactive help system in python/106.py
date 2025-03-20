def ajuda(com):
    help(com)

comando = ''

while True:
    print('-'*40)
    print('SISTEMA DE AJUDA EM PYTHON')
    print('-'*40)
    print('Digite "fim" para encerrar o programa')
    print('-'*40)
    comando = input('Função ou biblioteca >')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)