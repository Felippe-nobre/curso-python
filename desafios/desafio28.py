try:
    arquivo = open("novo_arquivo.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except IOError:
    print("Erro: Arquivo não encontrado.")
finally:
    arquivo.close()
    