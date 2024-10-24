import json
dados = {"nome": "ps5", "preço": 5000, "quantidade": 10}
with open("arquivo.json", "w") as arquivo:
    json.dump(dados,arquivo)

import json
with open("arquivo.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)