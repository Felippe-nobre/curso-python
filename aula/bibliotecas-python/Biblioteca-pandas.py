#Estruturas de dados principais do Pandas
'''As duas principais estruturas de dados oferecidas pelo Pandas são:

- **Series**: Uma estrutura de dados unidimensional, semelhante a uma lista ou coluna de uma planilha.
- **DataFrame**: Uma estrutura de dados bidimensional que se assemelha a uma tabela, com linhas e colunas'''

import pandas as pd
#Criando uma Series
#Você pode criar uma Series a partir de uma lista ou dicionário:
listas = [10,20,30,40]
serie = pd.Series(listas)
print(serie)

#Criando um DataFrame
#O DataFrame é a estrutura de dados mais poderosa do Pandas. Você pode criá-lo a partir de listas, dicionários, ou até mesmo de arquivos como CSV e Excel.
dados = {
    "Nome": ["Ana", "João", "Maria"],
    "Idade": [28, 34, 29],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Curitiba"]
}

df = pd.DataFrame(dados)
print(df)

# Manipulação de dados com Pandas
#Uma das grandes vantagens do Pandas é a facilidade com que você pode manipular dados. Vamos explorar algumas operações comuns.
print(df["Nome"])#Para selecionar uma coluna, use df['NomeColuna']:

print(df.iloc[0])#Para selecionar linhas, use iloc (baseado em índices) ou loc (baseado em rótulos):
print(df[df["Idade"] > 30])

# Adicionando e removendo colunas
#Você pode adicionar uma nova coluna ao DataFrame de forma simples:
df["Profissão"] = ["Engenheira", "Advogado", "Progamador"]
print(df)
df = df.drop(columns=["Cidade"])# drop: utilizado para remover colunas
print(df)

#Operações de agrupamento e agregação
#O Pandas facilita a análise de dados agrupando e agregando informações, o que é útil para criar relatórios e estatísticas.
dados_vendas = {
    "Vendedor": ["Ana", "Ana", "João", "Maria", "Maria"],
    "Vendas": [200, 150, 300, 400, 350]
}
df_vendas = pd.DataFrame(dados_vendas)

agrupado = df_vendas.groupby("Vendedor").sum()
print(agrupado)

#Leitura e escrita de arquivos
#O Pandas facilita a leitura e escrita de arquivos em diferentes formatos, como CSV, Excel, JSON, entre outros.
df.to_csv("saida.csv", index=False)

df_csv = pd.read_csv("arquivo.csv")
print(df_csv.head())