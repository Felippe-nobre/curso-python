
with open("imagem_origem.jpg", "rb") as arquivo_origem:
    conteudo = arquivo_origem.read()

with open("imagem_copia.jpg", "wb") as arquivo_copia:
    arquivo_copia.write(conteudo)
