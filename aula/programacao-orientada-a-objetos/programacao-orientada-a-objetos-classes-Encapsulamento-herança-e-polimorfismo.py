'''Encapsulamento

O encapsulamento permite proteger os atributos e métodos de um objeto, controlando o acesso a eles. Em Python, usamos `_` (underscore) para indicar que um atributo ou método é "privado".'''

class contaBancaria:
    def __init__(self,saldo):
        self.saldo = saldo
    
    def exibir_saldo(self):
        return f"Seu saldo é {self.saldo}"
    
conta = contaBancaria(1000)
print(conta.exibir_saldo())

'''### Herança

A herança permite que uma classe (classe filha) herde atributos e métodos de outra classe (classe pai).'''
class Animal:
    def __init__(self, nome):
        self.nome = nome
    def falar(self):
        pass
class cachorro(Animal):
    def falar(self):
        return "au au"
    
c = cachorro("Zeus")
print(c.falar())

'''### Polimorfismo

O polimorfismo permite que um método tenha comportamentos diferentes dependendo do objeto que o utiliza.'''
class Gato(Animal):
    def falar(self):
        return "Miau"
animais = [cachorro("Zeus"), Gato("Tom")]

for animal in animais:
    print(f"{animal.nome} diz: {animal.falar()}")

