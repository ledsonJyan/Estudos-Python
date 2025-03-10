from datetime import date
a=int(input('Em que ano você nasceu?:'))
hoje= date.today().year
c= date - a
if 9>c:
    print('sua idade é:',c)
    print('Sua classe é mirim')
elif 9<=c<14:
    print('sua idade é:',c)
    print('Sua clase é infantil')
elif 14<=c<19:
    print('sua idade é:',c)
    print('Sua classe é junior')
elif 19<=c<=25:
    print('sua idade é:',c)
    print('Sua clsse é sênior')
elif 25<c:
    print('sua idade é:',c)
    print('Sua classe é master')
