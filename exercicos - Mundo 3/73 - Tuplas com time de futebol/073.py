times = 'corinthians', 'palmeiras', 'santos', 'gremio', 'cruzeiro', 'flamengo', 'vasco', 'chapecoense', 'atletico', 'botafogo', 'atletico - PR', 'bahia', 'são paulo', 'fluminense', 'esport recife', 'ec vitiria', 'coritiba', 'avai', 'ponte preta', 'atletico - GO'
print(f'Os 5 primeiros colocados: {times[0:5]}\n')
print(f'Os ultimos 4 colocados: {times[-4:]}\n')
print(f'times em ordem alfabetica: {sorted(times)}\n')
print('chapecoense esta na posição:',times.index('chapecoense')+1)