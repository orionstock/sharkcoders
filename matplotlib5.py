from matplotlib import pyplot as plt
import numpy as np


x = np.arange(1, 16)
y = x**2

plt.subplot(2, 1, 1)
plt.plot(x, y, color='purple', marker='o')
plt.title("Quadrados dos Primeiros 15 Números")
plt.xlabel("Número")
plt.ylabel("Quadrado")
plt.grid(True)



plt.subplot(2, 1, 2)
plt.scatter(x, y, marker='x')
plt.title("Dispersão")
plt.xlabel("Índice")
plt.ylabel("Valor")



plt.tight_layout()
plt.show()