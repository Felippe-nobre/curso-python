'''
POO permite representar conceitos do mundo real em código, facilitando a modelagem de problemas complexos. Ela é baseada em quatro pilares fundamentais:

1. **Abstração**: Focar nos detalhes essenciais de um objeto e ignorar os detalhes irrelevantes.
2. **Encapsulamento**: Proteger os dados do objeto, permitindo acesso apenas por métodos específicos.
3. **Herança**: Reutilizar código definindo uma hierarquia entre classes.
4. **Polimorfismo**: Capacidade de um método se comportar de diferentes formas, dependendo do objeto que o utiliza.
'''


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