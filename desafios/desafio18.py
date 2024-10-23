import calculadora
num1 = float(input("digite um numero: "))
num2 = float(input("digite um numero: "))
operadores = input("digite um operador (+, -, *, /): ")

if operadores == "+":
   resultado = calculadora.soma(num1, num2)
elif operadores == "-":
   resultado = calculadora.subtracao (num1, num2)
elif operadores == "*":
    resultado = calculadora.multiplicacao(num1, num2)
elif operadores == "/":
    if num2 == 0:
       resultado = print("Erro!")
    else:
        resultado = calculadora.divisao (num1, num2)
print(f"O resultado é: {resultado}")
