#Trabalhando com arquivos binários
#Além de arquivos de texto e CSV, você pode manipular arquivos binários, como imagens, arquivos executáveis, entre outros.

with open("copia_imagem.png", "wb") as arquivo_binario:
    arquivo_binario.write(conteudo)

with open("imagem.png", "rb") as arquivo_binario:
    conteudo = arquivo_binario.read()
    print(conteudo)

