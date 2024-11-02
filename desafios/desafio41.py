import matplotlib.pyplot as plt


cidade1 = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42]
cidade2 = [18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

plt.plot(meses, cidade1, label="Cidade 1")
plt.plot(meses, cidade2, label="Cidade 2")
plt.xlabel("Meses")
plt.ylabel("temperatura média")
plt.title("temperatura média em duas cidades")
plt.legend()
plt.show()
