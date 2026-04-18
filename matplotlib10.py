import numpy as np
from matplotlib import pyplot as plt

num_points = 100
dt = 0.1

t_values = np.linspace(0, num_points * dt, num_points)
y_values = np.sin(t_values)

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(t_values, y_values)

ax.set_ylim(-1.1, 1.1)
ax.set_title("Sliding Window (No Animation Module)")

t_passed = 0;

while True:
    t_values = np.linspace(t_passed, t_passed + 100 * dt, 100)
    y_values = np.sin(t_values)

    ax.cla()
    ax.plot(t_values, y_values)
    ax.set_xlim(t_values[0], t_values[-1])

    plt.pause(0.1)
    t_passed += dt


