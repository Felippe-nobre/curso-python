#Conjuntos são coleções não ordenadas e sem elementos duplicados. Pense neles como uma caixa de lápis de cor 🎨, onde cada cor aparece apenas uma vez.
conjunto = {1,2,2,3,4,4}
print(conjunto)
a ={1,2,3}
b = {3,4,5}
conjunto.add(5)#Adiciona um elemento ao conjunto.
print(conjunto)
conjunto.remove(2)#Remove um elemento específico.
print(conjunto)
print(a | b) # União: {1, 2, 3, 4, 5}
print(a & b) # Interseção: {3}
print(a - b) # Diferenca: {1, 2}
