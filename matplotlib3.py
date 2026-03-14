from matplotlib import pyplot as plt
import numpy as np

numeros = np.random.uniform(0, 50, 100)


plt.subplot(2, 1, 1)
plt.hist(numeros, bins=10, color='skyblue', edgecolor='black')
plt.title("Histograma")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


indices = np.arange(len(numeros))


plt.subplot(2, 1, 2)
plt.scatter(indices, numeros, color='purple')
plt.title("Dispersão")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.tight_layout()

plt.show()