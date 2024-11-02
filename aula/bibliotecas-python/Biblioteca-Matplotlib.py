
import matplotlib.pyplot as plt


'''O Matplotlib é uma biblioteca poderosa para a visualização de dados em Python. Ele permite criar uma ampla variedade de gráficos e visualizações, desde os mais simples até os mais complexos, tornando-se uma ferramenta essencial para cientistas de dados, analistas e programadores que desejam comunicar informações de forma visual.'''

#Criando gráficos básicos

#Criando gráficos básicos
#O gráfico de linhas é ideal para mostrar tendências ao longo do tempo. Vamos criar um gráfico simples com o Matplotlib.
#Dados
anos = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
vendas = [100, 120, 150, 170, 160, 180]

#Criando o gráfico
plt.plot(anos,vendas, label="Vendas", color="red", marker ='o')
plt.title("Vendas por ano")
plt.xlabel("Anos")
plt.ylabel("Vendas(milhares)")
plt.legend()
plt.show()