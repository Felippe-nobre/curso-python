try:
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite um numero: "))
    resultado = num1 / num2
    print("O resultado é: ", resultado)
except ZeroDivisionError:
    print("Erro! Divisão por zero.")