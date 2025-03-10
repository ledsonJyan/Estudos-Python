p=float(input('Qual o seu peso?'))
a=float(input('Qual a sua altura?'))
imc= p/a**2

if imc<18.5:
    print('Você esta abaixo do peso')
elif 18.5<=imc<24.9:
    print('Você esta no peso normal')
elif 24.9<=imc<29.9:
    print('Você esta com sobre peso')
elif 29.9<=imc<34.9:
    print('Você esta com obesidade grau 1')
elif 34.9<=imc<39.9:
   print('Você esta com obesidade grau 2')
elif 39.9<imc:
    print('Você esta com obesidade grau 3')