import datetime 
dados = dict()

while True:
    nome = input('Nome = ')
    ano = int(input('Ano que nasceu: '))
    ctps = int(input('Numero da carteira de trabalho (0 se não tiver)'))
    
    if ctps == 0:
        break 
    
    if not ctps == 0:
     contrataçao = int(input('Ano de contratação: '))
     salario = float(input('Salario = '))
     
    break
    
data_atual = datetime.datetime.now()
idade = data_atual.year - ano

dados['nome'] = nome
dados['ano de nascimento'] = ano
dados['ctps'] = ctps
if not ctps == 0:
    dados['ano de contrataçao'] = contrataçao
    dados['salario'] = salario
    dados['aposentadoria'] = (dados['ano de contrataçao'] + 35) - ano 
print('-='*40)
print(dados)
print('-='*40)
print(f'O nome é: {nome}')
print(f'a idade é: {idade}')
print(f'Ctps: {ctps}')
if not ctps == 0:
    print(f'Ano de contratação: {contrataçao}')
    print(f'Salario: {salario}')
    print(f'A idade de aposentadoria é: {dados["aposentadoria"]}')
