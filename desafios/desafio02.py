num1 = float(input("Digite um numero:"))
num2 = float(input("Digite um numero:"))
operador = input("Digite um operador (+, -, *, /)+: ")
if operador == "+":
    print(num1 + num2)
elif operador == "-":
    print(num1 - num2)
elif operador == "*":
    print(num1 * num2)
elif operador == "/":
    if num2 == 0:
        print("Erro! Divisão por zero.")
    else:
        print(num1 / num2)
   