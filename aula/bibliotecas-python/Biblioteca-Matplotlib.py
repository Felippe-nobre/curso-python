
import matplotlib.pyplot as plt


'''O Matplotlib é uma biblioteca poderosa para a visualização de dados em Python. Ele permite criar uma ampla variedade de gráficos e visualizações, desde os mais simples até os mais complexos, tornando-se uma ferramenta essencial para cientistas de dados, analistas e programadores que desejam comunicar informações de forma visual.'''

#Criando gráficos básicos

#Criando gráficos linhas
#O gráfico de linhas é ideal para mostrar tendências ao longo do tempo. Vamos criar um gráfico simples com o Matplotlib.

#Dados
anos = [1960, 1970, 1980, 1990, 2000, 2010]
vendas = [100, 120, 150, 170, 160, 180]

#Criando o gráfico
plt.plot(anos, vendas, label="Vendas", color="purple", marker ='o')
plt.title("Vendas ao longo dos anos")
plt.xlabel("Ano")
plt.ylabel("Vendas (milhares)")
plt.legend()
plt.show()


#Gráfico de barras
#O gráfico de barras é ideal para comparar valores entre diferentes categorias.

categorias = ["A", "B", "C", "D"]
valores = [23, 45, 56, 78]

plt.bar(categorias, valores, color='green')
plt.title("Valores por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Valor")
plt.show()

# Gráfico de pizza
#O gráfico de pizza é útil para mostrar proporções de um todo.
fatias = [15, 30, 45, 10]
rotulos = ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4"]

plt.pie(fatias, labels=rotulos, autopct="%1.1f%%", startangle=90)
plt.title("Distribuição por Categoria")
plt.axis("equal")  # Assegura que o gráfico seja um círculo
plt.show()


#Personalizando gráficos
#Uma das maiores vantagens do Matplotlib é a capacidade de personalizar os gráficos para que eles se ajustem perfeitamente às suas necessidades.

#Alterando cores e estilos
#Você pode alterar as cores e estilos das linhas, barras e outros elementos do gráfico.
plt.plot(anos,vendas, color='red', linestyle='--', linewidth=2, marker='s')
plt.title("garfico personalizado")
plt.xlabel("anos")
plt.ylabel("vendas")
plt.show()

 #Adicionando múltiplas séries de dados
 #Você pode adicionar várias séries de dados em um único gráfico para comparações.
 # Dados
vendas_produto_A = [100, 120, 130, 145, 160, 180]
vendas_produto_B = [90, 110, 140, 150, 155, 170]

# Gráfico
plt.plot(anos, vendas_produto_A, label='Produto A', marker='o')
plt.plot(anos, vendas_produto_B, label='Produto B', marker='x')
plt.title("Comparação de Vendas entre Produtos A e B")
plt.xlabel("Ano")
plt.ylabel("Vendas")
plt.legend()
plt.show()

#Salvando gráficos
#Você pode salvar os gráficos em diferentes formatos de imagem, como PNG, JPG, SVG, etc.
plt.plot(anos, vendas, label='Vendas', marker='o')
plt.title("Vendas ao longo dos anos")
plt.xlabel("Ano")
plt.ylabel("Vendas (milhares)")
plt.legend()
plt.savefig("grafico_vendas.png")  # Salva o gráfico como PNG
plt.show()
