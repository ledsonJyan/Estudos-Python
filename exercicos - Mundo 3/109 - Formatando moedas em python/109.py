import moeda

numero =  -1

while numero != 0 :
    numero = float(input('Digite um numero qualquer (ou 0 para sair):'))
    
    if numero == 0:
        break
    
    print('-'*40)
    print('MENU')
    print('-'*40)
    opçao = int(input(' [1] Aumentar\n [2] Diminuir\n [3] Dobro\n [4] Metade\n'))
    
    if opçao == 1:
        escolha = int(input('Em quanto % quer aumentar?'))
        print(f'O aumento de {escolha}% de {moeda.moeda(numero)} é: {moeda.aumentar(numero,escolha)}\n')
    if opçao == 2:
        escolha = int(input('Em quanto % quer diminuir?'))
        print(f'A redução de {escolha}% de {moeda.moeda(numero)} é: {moeda.diminuir(numero,escolha)}\n')
    if opçao == 3:
        print(f'O dobro de {moeda.moeda(numero)} é: {moeda.dobro(numero)}\n')
    if opçao == 4:
        print(f'A metade de {moeda.moeda(numero)} é: {moeda.metade(numero)}\n')
    