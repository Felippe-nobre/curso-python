Num1 = float(input('primeira nota do aluno: '))
Num2 = float(input('Segunduna nota do aluno: '))
Num3 = float(input('Terceira nota do aluno: '))
soma = (Num1 + Num2 + Num3) / 3
if soma >= 7:
    print('Aprovado')
elif soma >= 5 and soma < 7:
        print('Recuperação')
else:
    print('Reprovado')
