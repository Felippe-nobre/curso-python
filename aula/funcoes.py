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

multiplicacao = lambda x: x*2#As funções lambda são funções anônimas (sem nome) que permitem criar pequenas funções em apenas uma linha. Elas são ideais para tarefas rápidas que não exigem a definição completa de uma função com def.
print(multiplicacao(5))
soma = lambda x,y: x+y
print(soma(5,8))

numeros = [1,2,3,4]
dobrado = list(map(lambda x: x * 2, numeros))#A função map() aplica uma função a cada item de um iterável (como uma lista) e retorna um novo iterável com os resultados.
print(dobrado)

Numeros = [1,2,3,4]
pares = list(filter(lambda x: x%2==0, Numeros))#A função filter() cria um iterável contendo apenas os itens que atendem a uma condição.
print(pares)

Nomes = ["Felipe", "Maria", "Joaquim"]
idades = [25,30,35]
combinado = list(zip(Nomes,idades))#A função zip() combina múltiplos iteráveis (listas, tuplas, etc.) em pares. É como fechar o zíper de uma jaqueta 🧥, onde os dentes de cada lado se unem.
print(combinado)

oi()
saudacao("Felippe")
saudacao2()

