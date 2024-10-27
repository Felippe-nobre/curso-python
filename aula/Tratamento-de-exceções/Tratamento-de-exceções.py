'''
## Introdução a erros e exceções

Erros em Python podem ser classificados em dois tipos:

- **Erros de Sintaxe**: Erros na forma como o código é escrito, impedindo a execução.
- **Exceções**: Erros que ocorrem durante a execução do código, mesmo que a sintaxe esteja correta (por exemplo, dividir por zero).
'''
numeros = int(input("Digite um número: "))
print((10 / numeros))# Se o usuário digitar 0, ocorrerá um erro "ZeroDivisionError"

