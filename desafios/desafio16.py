Nomes = ["Felipe", "Maria", "Joaquim", "Lucas"]
Nota =  [10.0,8.5,9.0,5.0]
combinacao = zip(Nomes, Nota)
for Nomes, Nota in combinacao:
    print(f"Nome: {Nomes}, Nota: {Nota}")