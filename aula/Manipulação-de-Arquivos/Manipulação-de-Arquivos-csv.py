
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