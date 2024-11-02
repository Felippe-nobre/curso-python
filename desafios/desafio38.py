import pandas as pd
Dados_vendas = pd.read_csv("vendas.csv")
total_vendas = Dados_vendas.groupby("Vendedor")['Valor da Venda'].sum()

print(total_vendas)