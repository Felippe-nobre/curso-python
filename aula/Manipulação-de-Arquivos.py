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


#Arquivos CSV (Comma-Separated Values) são comumente usados para armazenar dados tabulares. Python possui o módulo csv para facilitar a leitura e escrita desses arquivos.
#Lendo um arquivo CSV
import csv 
with open("dados.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)
# Escrevendo em um arquivo CSV
import csv
dados = [["Nome", "Idade"], ["Ana", 28], ["Carlos", 35]]

with open("dados.csv", "W", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)


#O JSON (JavaScript Object Notation) é um formato de armazenamento de dados muito utilizado para comunicação entre sistemas. Python possui o módulo json para manipular esses arquivos
#Escrevendo em um arquivo JSON
import json
dados = {"nome": "Ana", "idade": 28, "cidade": "São Paulo"}

with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo)
#Lendo um arquivo JSON
import json
with open("dados.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)
#Analogia: O JSON é como uma receita de culinária 🍴, onde as informações são armazenadas de forma estruturada e fácil de entender.

#Trabalhando com arquivos binários
#Além de arquivos de texto e CSV, você pode manipular arquivos binários, como imagens, arquivos executáveis, entre outros.

with open("copia_imagem.png", "wb") as arquivo_binario:
    arquivo_binario.write(conteudo)

with open("imagem.png", "rb") as arquivo_binario:
    conteudo = arquivo_binario.read()
    print(conteudo)

