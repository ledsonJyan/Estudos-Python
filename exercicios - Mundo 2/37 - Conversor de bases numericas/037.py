n = int(input("Digite um número inteiro qualquer: "))
print('Qual conversão você quer?\n [1] Binário\n [2] Octal\n [3] Hexadecimal\n')
op = int(input('Qual a sua opção? '))

if op == 1:
    print('O número {} em Binário: {}'.format(n, bin(n)[2:]))  
elif op == 2:
    print('O número {} em Octal: {}'.format(n, oct(n)[2:]))  
elif op == 3:
    print('O número {} em Hexadecimal: {}'.format(n, hex(n)[2:]))  
else:
    print("Opção inválida! Escolha entre 1, 2 ou 3.")