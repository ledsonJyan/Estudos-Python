n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
n3 = float(input('Terceira nota do aluno: '))
m = (n1 + n2 + n3) / 3  

if m >= 7:
    print("Você está APROVADO")
elif 5 <= m < 7:
    print("Você está de RECUPERAÇÃO")
else:
    print("Você está REPROVADO")