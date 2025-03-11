palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = 'AEIOU'


for palavra in palavras:
    
    vogais_na_palavra = [letra for letra in palavra if letra in vogais]
    
   
    print(f'Na palavra "{palavra}", tem as vogais: {", ".join(vogais_na_palavra)}')