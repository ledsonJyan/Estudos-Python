frase = input('Digite uma frase:').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for c in range(len(junto) - 1, -1, -1): 
    inverso += junto[c] 
print(junto,inverso)
if inverso==junto:
    print('É um palidromo')
else:
    print('Não é um palidromo')
 
