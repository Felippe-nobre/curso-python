#O bloco else é executado apenas se nenhuma exceção for gerada no bloco try.
try:
    numero = int(input("Digite um número: "))
    resultado = 10/ numero
except ZeroDivisionError:
    print("Erro: Não é possivel dividir por zero")
else:
    print("Resultado: ", resultado)