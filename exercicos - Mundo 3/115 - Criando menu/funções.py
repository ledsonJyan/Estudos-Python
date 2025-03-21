import time

def linha():
    print('-'*40)

def cabeçalho(menssagem):
    linha()
    print(menssagem.center(40))
    linha()

def iniciomenu():
    cabeçalho('MENU')
    

def menu():
    while True:
        print('Escolha entre 1, 2 e 3\n')
        try:
            escolha = int(input(' [1] Ver pessoas cadastradas\n [2] Cadastrar pessoas\n [3] Sair do sistema\n\n→ '))
            
            if escolha not in [1, 2, 3]:
                print('\nResposta inválida! Tente novamente.\n')
                time.sleep(1)
                continue

        except ValueError:
            print('\nEntrada inválida! Digite um número.\n')
            time.sleep(1)
            continue
        if escolha == 1:
            cabeçalho(f'Sua opção foi: {escolha} - Ver pessoas cadastradas')
            time.sleep(1)
        elif escolha == 2:
            cabeçalho(f'Sua opção foi: {escolha} - Cadastrar pessoas')
            time.sleep(1)
        elif escolha == 3:
            cabeçalho('Saindo do sistema...')
            time.sleep(1)
            break  

        
    