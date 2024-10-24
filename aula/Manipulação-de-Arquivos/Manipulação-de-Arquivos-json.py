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
