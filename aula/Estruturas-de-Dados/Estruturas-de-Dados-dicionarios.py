#Os dicionários são como um manual de instruções 📖, onde cada "palavra" tem um "significado". Eles armazenam pares de chave: valor.
dicionario = {"nome": "python", "ano": 2024, "tipo": "linguagem de programação"}
print(dicionario)
print(dicionario["nome"])
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
dicionario["ano"] = 2030
print(dicionario)
valor = dicionario.pop("ano")#Remove a chave e retorna seu valor.
print(dicionario)
valor = dicionario.get("ano", 2030)#Retorna o valor associado à chave, ou None se a chave não existir.
print(dicionario)
   