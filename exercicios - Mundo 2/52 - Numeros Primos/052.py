n = int(input('Digite um numero inteiro:'))
if n <=1:
    print('Esse numero não é primo')
else:
    for c in range (2,n):
        if  n %c==0:
            print('Esse numero não é primo')
            break
    else:
      print('Esse numero é primo')