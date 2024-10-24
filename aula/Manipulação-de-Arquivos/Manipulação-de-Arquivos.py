#A manipulação de arquivos de texto em Python é feita utilizando as funções open(), read(), write(), e close().
#- `'r'`: leitura (read). 'w': escrita (write) – cria um novo arquivo ou substitui o existente. 'a': adicionar (append) – adiciona conteúdo ao final do arquivo existente

arquivo = open("Exemplo.txt", "w")
arquivo.write("Olá, Python!")
arquivo.close()


arquivo = open("exemplo.txt", "r")#Para ler o conteúdo de um arquivo, use o método read().
conteudo = arquivo.read()
print(conteudo)  # Saída: Olá, Python!
arquivo.close()

with open("Exemplo.txt", "r") as arquivo: 
# Usando `with` para manipulação de arquivos. A palavra-chave `with` permite abrir e fechar arquivos de forma automática, tornando o código mais limpo e seguro.
    conteudo = arquivo.read()
    print(conteudo)




