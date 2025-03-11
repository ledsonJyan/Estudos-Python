lista = ('Camiseta', 29.00,
'Calça Jeans', 79.90,
'Tênis Esportivo', 90.00,
'Óculos de Sol', 59.00,
'Perfume', 40.00,
'Relógio de Pulso', 30.00,
'Cadeira Gamer', 599.00,
'Smartphone', 800.00,
'Fone de Ouvido Bluetooth', 25.00,
'Mochila', 89.90,
'Carregador Portátil', 25.00,
'Kit de Maquiagem', 129.90,
'Câmera Digital', 100.00,
'Caderno', 30.00,
'Console de Videogame', 2000.00)
for c in range(0,len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end ='')
    if c % 2 == 1:
        print(f'R${lista[c]:>7.2f}') 