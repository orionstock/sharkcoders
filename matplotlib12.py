import numpy as np
from matplotlib import pyplot as plt

plt.ion()

intensidade = []
indices = []

for i in range(100):
    valor = np.random.normal(-50, 5)

    if np.random.rand() < 0.05:
        valor += np.random.choice([-15, 15])

    intensidade.append(valor)
    indices.append(i)

    plt.clf()
    plt.title("Sinal Wi-Fi")
    plt.xlabel("Tempo")
    plt.ylabel("Intensidade (dBm)")

    intensidade_array = np.array(intensidade)
    indices_array = np.array(indices)


    outliers = intensidade_array < -70

    plt.plot(indices, intensidade, color="blue", label="Normal")
    plt.scatter(indices_array[outliers],
                intensidade_array[outliers],
                color="red", label="< -70 dBm")

    plt.axhline(-70, color='orange', linestyle='--', label='Limite -70 dBm')

    plt.legend()
    plt.pause(0.5)

plt.ioff()
plt.show()
