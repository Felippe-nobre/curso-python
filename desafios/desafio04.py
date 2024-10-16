# Funções para as operações
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

# Menu da calculadora
def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo da calculadora...")
            break

        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {soma(num1, num2)}")

            elif escolha == '2':
                print(f"{num1} - {num2} = {subtracao(num1, num2)}")

            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")

            elif escolha == '4':
                print(f"{num1} / {num2} = {divisao(num1, num2)}")

        else:
            print("Escolha inválida. Tente novamente.")

# Executando a calculadora
calculadora()
