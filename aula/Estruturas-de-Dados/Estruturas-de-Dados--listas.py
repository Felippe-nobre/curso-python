 #As listas são uma das estruturas de dados mais versáteis em Python. Pense nelas como uma prateleira de livros 📚, onde cada livro ocupa uma posição específica e você pode acessar, adicionar ou remover livros quando quiser.
''''''
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
#len(lista) Retorna o número de elementos.
#max(lista)Retorna o maior e menor elemento.
#min(lista)Retorna o maior e menor elemento.
lista2 = [4,1,3,2,5,4]
lista2.sort()#Ordena a lista em ordem crescente.
print(lista2)


