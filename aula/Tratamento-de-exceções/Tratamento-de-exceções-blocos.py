#O bloco try permite que você execute um código que pode gerar uma exceção. O bloco except captura e lida com a exceção, evitando que o programa seja interrompido.

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Não é possivel dividir por zero")
except ValueError:
    print("Erro: Você dever colocar um numero valido")