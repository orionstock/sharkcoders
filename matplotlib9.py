from matplotlib import pyplot as plt
import numpy as np

numeros = np.random.normal(2, 1, 600)

plt.subplot(1, 3, 1)
plt.hist(numeros, bins=25, color='coral', edgecolor='gray')
plt.title("Histograma Normal")

potencias2 = np.arange(1, 11)
potencias22 = 2**potencias2

plt.subplot(1, 3, 2)
plt.bar(potencias2, potencias22, color='navy')
plt.title("Potências de 2")

x = np.random.rand(150)
y = np.random.rand(150)

plt.subplot(1, 3, 3)
plt.scatter(x, y, color="limegreen")
plt.title("Scatter Aleatório")



plt.show()