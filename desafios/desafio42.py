import matplotlib.pyplot as plt
cesto = ["maçãs", "bannas", "larnjas", "uvas"]
vendas = [40,25,20,15]

plt.pie(vendas, labels=cesto, autopct="%1.1f%%")
plt.title("Cesta de frutas")
plt.axis("equal")
plt.show()