#O bloco finally é executado independentemente de ocorrer uma exceção ou não. Ele é útil para liberar recursos, como fechar arquivos.

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
finally:
    arquivo.close()
    print("Arquivo fechado.")
