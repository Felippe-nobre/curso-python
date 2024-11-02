import pandas as pd

produtos = pd.DataFrame({
    "Nome": ["Ana", "João", "Maria"],
    "Preços": [28, 34, 29],
    "Quantidade em Estoque": [10, 20, 30],
    

})
produtos["valor_total"] = produtos["Preços"] * produtos["Quantidade em Estoque"]

produtos_mais_caros = produtos.loc[produtos["Preços"].idxmax()]
print(produtos_mais_caros)