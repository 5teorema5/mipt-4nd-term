import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Начальные параметры
m = 1  # масса
l = 1  # длина маятника
g = 10  # ускорение свободного падения
A = 0.1  # амплитуда
# omega = 25  # частота колебаний
b = 5  # коэффициент затухания

# Диапазон частот вибрации
omega_values = np.linspace(1, 120, 120)


# уравнение движения маятника Капицы
def kapitsa_pendulum(y, t, m, l, g, A, omega):
    theta, dtheta = y
    ddtheta = ((A * omega ** 2 * np.sin(omega * t)) / l - g / l) * np.sin(theta) - b * dtheta
    return dtheta, ddtheta


# Построение бифуркационной диаграммы
fig, ax = plt.subplots(dpi=80, figsize=(10, 6))

for omega in omega_values:
    y0 = [np.pi - 0.1, 0]  # Начальные условия (почти перевёрнутое положение)
    # интервал в 100 единиц времени, 10000 точек
    t = np.linspace(0, 100, 10000) # Долгое время для устранения переходных процессов

    # решатель ode45
    solution = odeint(kapitsa_pendulum, y0, t, args=(m, l, g, A, omega))
    theta = solution[:, 0]

    # берём значения theta в моменты, кратные периоду вибрации
    T = 2 * np.pi / omega  # Период вибрации
    strobe_indices = np.where(np.abs(t % T) < 0.01)[0]  # Моменты, близкие к t = nT
    strobe_theta = theta[strobe_indices]

    # Отображаем точки на диаграмме
    plt.plot([omega], strobe_theta[-1], 'bo', markersize=3, alpha=0.5)

ax.set_yticks([0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi, 2*np.pi])
ax.set_yticklabels(['0', 'π/4', 'π/2', '3π/4', 'π', '2π'])

plt.xlabel(r'Частота вибрации $\omega$')
plt.ylabel(r'Угол $\theta$')
plt.title(
    f'Бифуркационная диаграмма маятника Капицы,\nкоэффициент затухания затухания b={b},\nамплитуда колебаний подвеса A={A}')
plt.grid(True)
plt.show()
