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