print('Escolha a PA que quiser e veja os 10 primeiros termos')
primeiro = int(input('Primeiro termo diferente de 0:'))
razao = int(input('Escolha a razao:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        
        print('{} - '.format(termo), end = '')
        termo += razao 
        cont += 1

    print ('PAUSA')
    mais = int(input('Quantos termos você quer mostar a mais?'))
print('Fim do programa')
print('Foram mostrados {} termos'.format(total))