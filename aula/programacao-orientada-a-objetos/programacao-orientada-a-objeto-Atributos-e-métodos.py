'''### Atributos de instância

Os atributos de instância são definidos dentro do método `__init__` e são exclusivos de cada objeto.'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Felippe", 21)
p2 = Pessoa("Danilo", 21)

'''### Métodos de instância

Métodos são funções que pertencem à classe e podem acessar os atributos do objeto usando `self`.'''

class pessoa:
    def __init__(self, nome):
        self.nome = nome
        
    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}"
    
p = pessoa("Felippe")
print(p.cumprimentar())

