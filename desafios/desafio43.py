import matplotlib.pyplot as plt
loja1 = ["Ps5", "xbox", "switch", "pc", "tv"]
quantidade_de_vendas1 = [10, 20, 30, 40, 50]

loja2 = ["Ps5", "xbox", "switch", "pc", "tv"]
quantidade_de_vendas2 = [5, 10, 15, 60, 80]

plt.plot(loja1, quantidade_de_vendas1, label = "loja 1", color = "red", linestyle = "-", linewidth = 2, marker = "s")
plt.plot(loja2, quantidade_de_vendas2, label = "loja 2", color = "blue", linestyle = "-", linewidth = 3, marker = "s")
plt.title("lojas com mais vendas")
plt.xlabel("Loja")
plt.ylabel("Quantidade de vendas")
plt.show()