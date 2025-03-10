import time 
print('CONTAGEM REGRESSIVA PARA A QUEIMA DE FOGOS')
n=input('Pronto? (sim ou não)').upper()
if n=='SIM':  
  for c in range(10,0,-1):
    print(c)
    time.sleep(1)
  print('FELI ANO NOVO')
elif n=='NAO' or n=='NÃO':
    print('Volte sempre')
else:
    print('Resposta diferente de sim ou não')