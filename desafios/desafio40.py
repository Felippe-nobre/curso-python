import matplotlib.pyplot as plt
produtos = ["Ps5", "xbox", "switch", "pc", "tv"]
quantidade_de_vendas = [10, 20, 30, 40, 50]

plt.barh(produtos,quantidade_de_vendas, color="purple")
plt.title("Produtos mais vendidos")
plt.xlabel("Quantidade de vendas")
plt.ylabel("Produtos")
plt.show()
