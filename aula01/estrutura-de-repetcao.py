nomes = ["Felippe", "Maria", "Joaquim", "Lucas"]
for nome in nomes:
    print("Olá: ", nome)

for i  in range(5):  # O range() gera uma sequência de números. Ele é muito útil em conjunto com for.
    print(i)

contador = 0
while contador < 5:
    print("Contagem", contador)
    contador += 1

for numero in range(10):
    if numero == 5:
        break
    print(numero)

for numero in range(5):
    if numero == 2:
        continue
    print(numero)

for i in range(3):
    pass