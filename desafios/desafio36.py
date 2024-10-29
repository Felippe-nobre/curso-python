import numpy as np

matriz1 = np.array([[2,3],
                     [1,4]])
matriz2 = np.array([[5,6], 
                    [7,8]])
resultado = np.dot(matriz1,matriz2)
print("Matriz1:\n",matriz1)
print("Matriz2:\n",matriz2) 
print("Matriz1 x Matriz2:\n", resultado)