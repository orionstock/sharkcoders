from matplotlib import pyplot as plt
import numpy as np

numeros = np.random.normal(0, 1, 1000)

plt.subplot(2, 1, 1)
plt.hist(numeros, bins=30, color='skyblue', edgecolor='black')
plt.title("Histograma: Distribuição Normal")



x = np.random.rand(100)
y = np.random.rand(100)


plt.subplot(2, 1, 2)
plt.scatter(x, y, color="red")
plt.title("Scatter Plot Aleatório")
plt.xlabel("X")
plt.ylabel("Y")


plt.tight_layout()
plt.show()