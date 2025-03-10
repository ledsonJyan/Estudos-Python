n1 = float(input('Digite um numero:'))
n2 = float(input('Digite outro numero:'))
opçao = 0
while opçao!= 0.5:
  opçao = float(input(' [1] Soma\n [2] Multiplicação\n [3] Maior\n [4] Novos numeros\n [0.5] Encerrar o programa\n'))
  if opçao == 1:
       soma = n1 + n2
       print('A soma é: {}\n'. format(soma))
  if opçao == 2:  
        multiplicacao = n1 * n2
        print('A multiplicação dos números é: {}\n'.format(multiplicacao))
  if opçao == 3:
        if n1>n2:
              maior = n1
              print('O maior numero é: {}'.format(n1))
        else:
              maior = n2
              print('O maior numero é: {}'.format(n2))
  if opçao == 4:
        print('Informe os novos numeros')
        n1 = float(input('Digite um numero:'))
        n2 = float(input('Digite outro numero:'))
  if opçao == 0.5:
      print('Programa encerrado')
  else: 
        print('Numero diferente de 1,2,3,4 e 0.5, tente novamente')


