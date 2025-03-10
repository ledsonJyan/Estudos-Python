from datetime import date
i = int(input('Em que ano você nasceu?: '))
hoje= date.today().year
ia = hoje - i  # Idade atual
r = int(input('Você já se alistou? (responda com sim=1 ou não=0): '))

if ia == 18:
    if r == 1:
        print('Obrigado pelo seu serviço.')
    else:
        print('Está na hora de se alistar no exército.')
elif ia < 18:
    print(f'Falta {18 - ia} anos para você se alistar no exército.')
elif ia > 18 and r == 1:
    print('Obrigado pelo seu serviço.')
elif ia > 18 and r == 0:
    print(f'Você está atrasado {ia - 18} anos para se alistar.')

   

