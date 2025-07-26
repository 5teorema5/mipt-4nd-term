import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Параметры системы
m = 1.0       # масса маятника (кг)
L = 1.0       # длина стержня (м)
g = 9.81      # ускорение свободного падения (м/с²)
A = 0.1       # амплитуда вибрации подвеса (м)
omega = 20.0  # частота вибрации (рад/с)

# Уравнение движения маятника Капицы
def kapitsa_pendulum(y, t, m, L, g, A, omega):
    theta, dtheta = y
    ddtheta = ( (A * omega**2 * np.sin(omega * t)) / L - g / L ) * np.sin(theta)
    return [dtheta, ddtheta]

# Начальные условия
theta0 = np.pi - 0.1  # почти перевёрнутое положение
dtheta0 = 0.0
y0 = [theta0, dtheta0]

# Временной интервал
t = np.linspace(0, 10, 500)  # 10 секунд, 500 кадров

# Решение уравнения
solution = odeint(kapitsa_pendulum, y0, t, args=(m, L, g, A, omega))
theta = solution[:, 0]

# 3D-координаты
x = L * np.sin(theta)          # движение в плоскости x-z
y = np.zeros_like(x)           # y = 0 (можно добавить движение по y для сложных траекторий)
z_pivot = A * np.sin(omega * t)  # вибрация подвеса по z
z_bob = z_pivot - L * np.cos(theta)  # z-координата груза

# Создание 3D-графика
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1.5*L, 1.5*L)
ax.set_ylim(-1.5*L, 1.5*L)
ax.set_zlim(-1.5*L, 1.5*L)
ax.set_xlabel('X (м)')
ax.set_ylabel('Y (м)')
ax.set_zlabel('Z (м)')
ax.set_title('3D-модель маятника Капицы (ω = {} рад/с)'.format(omega))

# Инициализация объектов анимации
line, = ax.plot([], [], [], 'b-', lw=2)
point, = ax.plot([], [], [], 'ro', ms=10)
pivot_point, = ax.plot([], [], [], 'ko', ms=6)
time_text = ax.text2D(0.02, 0.95, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    pivot_point.set_data([], [])
    pivot_point.set_3d_properties([])
    time_text.set_text('')
    return line, point, pivot_point, time_text

def animate(i):
    # Положение подвеса (колеблется по z)
    pivot_x = 0
    pivot_y = 0
    pivot_z = z_pivot[i]

    # Положение груза
    bob_x = x[i]
    bob_y = y[i]
    bob_z = z_bob[i]

    # Обновление линии (стержень) и точки (груз)
    line.set_data([pivot_x, bob_x], [pivot_y, bob_y])
    line.set_3d_properties([pivot_z, bob_z])
    point.set_data([bob_x], [bob_y])
    point.set_3d_properties([bob_z])
    pivot_point.set_data([pivot_x], [pivot_y])
    pivot_point.set_3d_properties([pivot_z])
    time_text.set_text(f'Время: {t[i]:.2f} с')

    return line, point, pivot_point, time_text

# Запуск анимации
ani = FuncAnimation(fig, animate, frames=len(t), init_func=init,
                    blit=True, interval=20, repeat=True)

plt.tight_layout()
plt.show()