'''O NumPy (Numerical Python) é uma das bibliotecas mais populares e fundamentais para a computação científica em Python. Ele fornece suporte para a manipulação eficiente de grandes vetores, matrizes e arrays multidimensionais, além de oferecer funções matemáticas de alto desempenho.
**Analogia**: Pense no NumPy como uma **calculadora científica superpotente** 🧮 que pode manipular grandes volumes de números de forma rápida e eficiente.'''

import numpy as np

lista = [1,2,3,4,5]
array = np.array(lista)
print(array)

matriz = np.array([[1,2,3], [4,5,6]])
print(matriz)


zeros = np.zeros((2,3))#np.zeros((linhas, colunas))`: Cria um array de zeros.
print(zeros)
ones = np.ones((2,3))  #np.ones((linhas, colunas))`: Cria um array de uns.
print(ones)
eye = np.eye(3) #np.eye(n)`: Cria uma matriz identidade.
print(eye)
arange = np.arange(0, 10, 2) #np.arange(início, fim, passo)`: Cria um array com valores em um intervalo.
print(arange)

#Operações aritméticas
#Podemos realizar operações aritméticas diretamente nos arrays, e o NumPy aplica as operações a todos os elementos:
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
soma = array1 + array2
print(soma)
multiplicacao = array1 * 2
print(multiplicacao)

#Indexação e fatiamento
#Você pode acessar e modificar elementos de um array de forma semelhante às listas.
array = np.array([10,20,30,40])
print(array[1])

matriz = np.array([[1,2,3], [4,5,6]])
print(matriz[1,2])

#Funções estatísticas
#NumPy oferece funções úteis para estatísticas e análise de dados:
array = np.array([1,2,3,4,5])
print((np.mean(array)))#np.mean(array): Média dos elementos.
print((np.sum(array)))#np.sum(array): Soma dos elementos.
print(np.max(array))#np.max(array): Maior valor.
print(np.min(array))#np.min(array): Menor valor.
print(np.std(array))#np.std(array): Desvio padrão dos elementos.

#Operações com matrizes
#NumPy facilita a manipulação e operação com matrizes, como a multiplicação de matrizes.
matriz1 = np.array([[1,2], [3,4]])
matriz2 = np.array([[5,6], [7,8]])
resultado = np.dot(matriz1,matriz2)#np.dot() realiza a multiplicação de matrizes e produtos escalares.
print(resultado)