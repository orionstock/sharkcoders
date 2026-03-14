from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y, color="red", linestyle="--", marker="o", label="fixemetro")
plt.legend()

plt.title("Gráfico fixe")
plt.xlabel("fixe 1")
plt.ylabel("fixe 2")

plt.show()