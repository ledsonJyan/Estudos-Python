dados = dict()  
lista = list()  

while True:
    dados['nome'] = input('Nome do jogador: ')  

    dados['partida'] = int(input(f'Quantas partidas {dados["nome"]} jogou? ')) 

    gols_por_partida = [] 
    
   
    for c in range(0, dados['partida']):
        gols = int(input(f'Quantos gols na partida {c + 1}? '))
        gols_por_partida.append(gols) 
    
    dados['gols_por_partida'] = gols_por_partida  

    lista.append(dados.copy())  

    
    while True:
        escolha = input('Quer continuar? [S/N] ').upper()
        if escolha not in ['S', 'N']:  
            print('Resposta inválida! Tente novamente.')
            continue
        if escolha == 'S' or escolha == 'N':
            break
    if escolha == 'N':
        break


print("\nJogadores e seus gols:")
for jogador in lista:
    print(f"{jogador['nome']} jogou {jogador['partida']} partidas.")
    print(f"Gols por partida: {jogador['gols_por_partida']}")
