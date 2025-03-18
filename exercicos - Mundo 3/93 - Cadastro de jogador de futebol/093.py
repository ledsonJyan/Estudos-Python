dados = dict()
lista = list()
nome = input('Nome do jogador:')
cont_gols = 0
partida = int(input(f'Quantos partidas {nome} jogou?'))
for c in range(0,partida):
    gols = int(input(f'Quantos gols na partida {c + 1}:'))
    cont_gols += gols
    lista.append(gols)
dados['jogador'] = nome
dados['gols na partida'] = lista
dados['total'] = cont_gols
print('-='*40)
print(dados)
print('-='*40)
print(f'O campo nome tem o valor {nome}')
print(f'O campo gols tem o valor {lista}')
print(f'O campo total tem o valor {cont_gols}')
print('-='*40)
print(f'O jogador {nome} jogou {partida} partidas')
for c in range(partida):
    print(f'  Na partida {c + 1}, fez {lista[c]} gols')
print(f'Foi um total de {cont_gols} gols')