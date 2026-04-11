from matplotlib import pyplot as plt
import numpy as np

numeros = np.random.normal(0, 1, 500)

plt.subplot(1, 2, 1)
plt.hist(numeros, bins=10, color='orange', edgecolor='black')
plt.title("Histograma: 10 bins")

plt.subplot(1, 2, 2)
plt.hist(numeros, bins=50, color='teal', edgecolor='black')
plt.title("Histograma: 50 bins")

plt.tight_layout()
plt.show()