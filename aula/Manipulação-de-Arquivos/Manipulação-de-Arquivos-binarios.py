#Trabalhando com arquivos binários
#Além de arquivos de texto e CSV, você pode manipular arquivos binários, como imagens, arquivos executáveis, entre outros.

with open("imagem_origem.jpg", "rb") as arquivo_origem:
    conteudo = arquivo_origem.read()

with open("imagem_copia.jpg", "wb") as arquivo_copia:
    arquivo_copia.write(conteudo)
