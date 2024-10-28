#Uma classe é um "molde" que define as características e comportamentos de um objeto. Um objeto é uma instância dessa classe.


class Carro:
    
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def descrever(self):
        return f"{self.marca} {self.ano} {self.modelo}"
    
meu_carro = Carro("Toyta", "Corolla", 2020)
print(meu_carro.descrever())