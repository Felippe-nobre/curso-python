import pandas as pd

dados  = pd.DataFrame ({
    "Alunos": ["Felippe", "LUiz", "Maria"],
    'Matemática': [8.0, 6.5, 7.2],
    'Física': [9.0, 7.0, 8.1],
    'Química': [7.5, 8.2, 6.9]
})
df = pd.DataFrame(dados)
df['Média'] = (df['Matemática'] + df['Física'] + df['Química']) / 3
print(df)