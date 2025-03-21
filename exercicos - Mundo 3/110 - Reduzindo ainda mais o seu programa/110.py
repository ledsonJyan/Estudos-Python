from moeda import resumo
numero =  -1

while numero != 0 :
    numero = float(input('Digite um numero qualquer (ou 0 para sair):'))
    
    if numero == 0:
        break
    
    resumo()