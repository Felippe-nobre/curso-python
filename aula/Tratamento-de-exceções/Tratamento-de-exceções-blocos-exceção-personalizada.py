#Para criar uma exceção personalizada, basta criar uma nova classe que herde de Exception.
class  ErroPersonalizado(Exception):
    pass
def verficar_idade(idade):
    if idade < 18:
        raise ErroPersonalizado("Idade menor que 18 não é permitida")
    else:
        print("Acesso permitido.")

try:
    verficar_idade(16)
except ErroPersonalizado as e:
    print(e)