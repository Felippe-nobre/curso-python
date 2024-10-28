class veiculo:
    def mover(self):
        return "O veículo está se movendo."
class carro(veiculo):
    def mover(self):
        return"O carro está andando na estrada."
class bicicleta(veiculo):
    def mover(self):
        return "A bicicleta está sendo pedalada na ciclovia."

meu_carro = carro()
minha_bicicleta = bicicleta()

print(meu_carro.mover())
print(minha_bicicleta.mover())