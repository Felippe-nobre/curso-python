import csv

with open("arquivo.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    next(leitor)
    for linha in leitor:
        notas = list(map(float, linha[1:],))
        media = sum(notas) / len(notas)
        print(f"Nomes {linha[0]}: {media:.2f}")