def ficha(a =0, b = 0):
    if a == '':
        a = '<desconhecido>'
    if b == '':
        b = 0
    print(f'O jogador {a} marcou {b} gol(s) no campeonato')
jogador = input('Qual o nome do jogador?')
gol = input('Quantos gol(s) ele marcou?')
ficha(jogador,gol)
