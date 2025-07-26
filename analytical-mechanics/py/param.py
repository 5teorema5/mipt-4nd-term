import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Начальные параметры
m = 1  # масса
l = 1  # длина маятника
g = 10  # ускорение свободного падения
A = 0.1  # амплитуда
# omega = 25  # частота колебаний
# omega = 50
omega = 6.32
b = 0  # коэффициент затухания
I = m * l ** 2  # момент инерции

# начальные параметры
# theta0 = np.pi - 0.1  # начальный угол отклонения от вертикали
theta0 = 0
dtheta0 = 0.1  # начальная производная угла отклонения
y0 = [theta0, dtheta0]


# уравнение движения маятника Капицы
def kapitsa_pendulum(y, t, m, l, g, A, omega):
    theta, dtheta = y
    ddtheta = ((A * omega ** 2 * np.sin(omega * t)) / l - g / l) * np.sin(theta) - b * dtheta
    return dtheta, ddtheta


# интервал в 100 единиц времени, 10000 точек
t = np.linspace(0, 100, 10000)

# решатель ode45
solution = odeint(kapitsa_pendulum, y0, t, args=(m, l, g, A, omega))
theta = solution[:, 0]

# координаты груза
x = l * np.sin(theta)
y = -l * np.cos(theta) + A * np.sin(omega * t)

# отрисовка
fig = plt.figure(figsize=(8, 8))
plt.subplots_adjust(bottom=0.1)
axis = plt.axes(xlim=(-1.5 * l, 1.5 * l), ylim=(-1.5 * l, 1.5 * l))
axis.set_aspect('equal', adjustable='box')

plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

line, = axis.plot([], [], 'k-', lw=2)
point, = axis.plot([], [], 'ro', ms=10)
tr, = axis.plot([], [], '-g', lw=1)
time_text = axis.text(0.02, 0.95, '', transform=axis.transAxes)

x_tr, y_tr = [], []


def init():
    line.set_data([], [])
    point.set_data([], [])
    x_tr = []
    y_tr = []
    tr.set_data(x_tr, y_tr)
    time_text.set_text('')
    return line, point, time_text,


def animate(i):
    pivot_x = 0
    pivot_y = A * np.sin(omega * t[i])
    line.set_data([pivot_x, x[i]], [pivot_y, y[i]])
    point.set_data(x[i], y[i])
    x_tr.append(x[i])
    y_tr.append(y[i])
    tr.set_data(x_tr, y_tr)
    time_text.set_text(f'Время: {t[i]:.2f} c')
    return line, point, time_text, tr,


# анимация
ani = FuncAnimation(fig, animate, frames=len(t), interval=2, blit=True, repeat=True)
print(x_tr)
plt.title(fr'Маятник Капицы ($\omega$={omega})')
plt.xlabel('x (м)')
plt.ylabel('y (м)')
plt.plot(x_tr, y_tr)

plt.show()
