from math import factorial

escolha = 1


while escolha != 0:
    escolha = int(input('Digite o numero que você quer fatorar ou (digite 0 para sair):'))
    print('\n')
    if escolha == 0:
  
      print('O programa foi encerrado\n')
    
    else:
         resposta = factorial(escolha)
         print('A fatoração de {} é: {}\n'.format(escolha,resposta))

   

