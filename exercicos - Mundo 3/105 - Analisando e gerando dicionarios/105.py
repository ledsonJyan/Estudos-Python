
def notas(*num):
   dados = dict()
   dados['notas'] = len(num)
   dados['maior'] = max(num)
   dados['menor'] = min(num)
   dados['media'] = sum(num)/ len(num)
   if dados['media'] >= 7:
       dados['situação'] = 'BOA'
   if 5 <= dados['media'] <= 6.99:
       dados['situação'] = 'RAZOALVEL'
   if dados['media'] < 5:
       dados['situação'] = 'RUIM'

   return dados
resposta = notas(8.5, 7.0, 5.8, 10)
print(resposta)
       
