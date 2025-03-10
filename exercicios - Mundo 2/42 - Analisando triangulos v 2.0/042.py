s1=float(input('Primeiro segmento:'))
s2=float(input('Segundo segmento:'))
s3=float(input('Terceiro segmento:'))

if s1< s2 + s3 and s2<s3 +s1 and s3< s1 + s2:
    print('Esses segmentos podem formar um triangulo')
    if s1==s2==s3:
        print('EQUILATERO')
    elif s1!= s2!= s3:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Esses segmentos não podem formar um triangulo')