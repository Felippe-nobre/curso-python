 #As listas são uma das estruturas de dados mais versáteis em Python. Pense nelas como uma prateleira de livros 📚, onde cada livro ocupa uma posição específica e você pode acessar, adicionar ou remover livros quando quiser.
lista = [1,2,3, "Python", True]
print(lista)
print(lista[0])
print(lista[3])
print(lista[-1])

lista.append("Novo item") #Adicionar: Use append() para adicionar um elemento ao final da lista.
print(lista)

lista.remove("Python")#Remover: Use remove() para remover um item específico, ou pop() para remover pelo índice.
print(lista)

lista.pop(0)#Remove o primeiro elemento
print(lista)

for item in lista:
    print(item)

#As tuplas são similares às listas, mas são imutáveis, ou seja, não podem ser alteradas depois de criadas. Pense nelas como o menu de um restaurante 🍽️. Uma vez que o menu está impresso, não é possível alterar as opções sem fazer um novo.
tulpa = (1,2,3,"Python", True)
print(tulpa)
print(tulpa[1])

#Conjuntos são coleções não ordenadas e sem elementos duplicados. Pense neles como uma caixa de lápis de cor 🎨, onde cada cor aparece apenas uma vez.
conjunto = {1,2,2,3,4,4}
print(conjunto)

a ={1,2,3}
b = {3,4,5}
print(a | b) # União: {1, 2, 3, 4, 5}
print(a & b) # Interseção: {3}
print(a - b) # Diferenca: {1, 2}

#Os dicionários são como um manual de instruções 📖, onde cada "palavra" tem um "significado". Eles armazenam pares de chave: valor.
dicionario = {"nome": "python", "ano": 2024, "tipo": "linguagem de programação"}
print(dicionario)
print(dicionario["nome"])

dicionario["ano"] = 2030
print(dicionario)
   