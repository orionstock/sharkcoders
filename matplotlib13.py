import numpy as np
from matplotlib import pyplot as plt

tempo = []
batimentos = []

for i in range(150):
    valor = np.random.normal(75, 3)

    if np.random.rand() < 0.02:
        valor += np.random.choice([5, 10])

    plt.clf()
    plt.title("Batimentos Cardíacos")
    plt.xlabel("Tempo")
    plt.ylabel("Batimentos (BPM)")

    tempo.append(valor)
    batimentos.append(i)

    batimentos_array = np.array(batimentos)

    limite = batimentos_array > 120


    tempo_array = np.array(tempo)


    plt.plot(batimentos, tempo, color="green", label="Normal")
    plt.scatter(batimentos_array[limite],
                tempo_array[limite],
                color="red", label="Anomalia")
    plt.legend()
    plt.pause(0.2)

plt.ioff()
plt.show()

