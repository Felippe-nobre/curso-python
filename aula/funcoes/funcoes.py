def oi():
    print("Olá, Mundo!")
def saudacao(nome):
    print(f"Seja bem-vindo, {nome}")

def saudacao2(nome="Visitante"):#Você pode definir um valor padrão para um parâmetro. Se nenhum valor for fornecido, o padrão será usado.
    print(f"Seja bem-vindo, {nome}")
def soma(a,b):
    return a + b#Uma função pode retornar um valor usando a palavra-chave return.
result = soma(5,3)
print(result)

oi()
saudacao("Felippe")
saudacao2()

