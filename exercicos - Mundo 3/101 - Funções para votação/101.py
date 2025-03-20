import datetime
def votaçao():
   hoje = datetime.datetime.now()
   idade = hoje.year - ano
   if 18 < idade < 65:
       print(f'Com {idade} anos votação é obrigatorio')
   if 16 < idade < 18:
        print(f'Com {idade} anos votação é opcional')
   if 65 <= idade:
       print(f'Com {idade} anos votação é opcional')
   if idade < 16:
       print(f'Com {idade} anos votação é proibida')  
   return idade  
ano = int(input('Ano de nacimento:'))
votaçao()