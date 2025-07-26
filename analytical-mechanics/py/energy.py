import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Начальные параметры
m = 1  # масса
l = 1  # длина маятника
g = 10  # ускорение свободного падения
A = 0  # амплитуда
omega = 25  # частота колебаний
# omega = 50
b = 0  # коэффициент затухания
I = m * l ** 2  # момент инерции

# начальные параметры
theta0 = np.pi - 0.1  # начальный угол отклонения от вертикали
# theta0 = .1
dtheta0 = 0.1  # начальная производная угла отклонения
y0 = [theta0, dtheta0]


# Уравнение движения маятника Капицы
def kapitsa_pendulum(y, t, m, l, g, A, omega):
    theta, dtheta = y
    ddtheta = ((A * omega ** 2 * np.sin(omega * t)) / l - g / l) * np.sin(theta) - b * dtheta
    return dtheta, ddtheta


# интервал в 10 единиц времени, 1000 точек
t = np.linspace(0, 10, 1000)

# решатель ode45
solution = odeint(kapitsa_pendulum, y0, t, args=(m, l, g, A, omega))
theta, dtheta = solution[:, 0], solution[:, 1]

# Координата y груза
y_pivot = A * np.sin(omega * t)  # Колебания подвеса
y_bob = y_pivot - l * np.cos(theta)  # Положение груза

# Скорость груза (производная y_bob)
v_y = A * omega * np.cos(omega * t) + l * dtheta * np.sin(theta)

# Энергии
U = m * g * y_bob  # Потенциальная энергия
T = 0.5 * m * ((l * dtheta) ** 2 + v_y ** 2)  # Кинетическая энергия
E_total = T + U  # Полная энергия

# Построение графика
plt.figure(figsize=(10, 5))
plt.plot(t, T, 'r-', label='Кинетическая (Т)')
plt.plot(t, U, 'b-', label='Потенциальная (П)')
plt.plot(t, E_total, 'g-', label='Полная (E)', alpha=0.7)
plt.xlabel('Время')
plt.ylabel('Энергия')
plt.title('Энергии маятника Капицы')
plt.legend()
plt.grid()
plt.show()
