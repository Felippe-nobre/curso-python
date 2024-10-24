
#As tuplas são similares às listas, mas são imutáveis, ou seja, não podem ser alteradas depois de criadas. Pense nelas como o menu de um restaurante 🍽️. Uma vez que o menu está impresso, não é possível alterar as opções sem fazer um novo.
tulpa = (1,2,3,"Python", True)
print(tulpa)
print(tulpa.count(1))#Conta quantas vezes o valor aparece na tupla.
print(tulpa.index(3))#Retorna o índice da primeira ocorrência do valor.
print(tulpa[1])