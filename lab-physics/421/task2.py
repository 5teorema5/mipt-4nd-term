from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})


def func(x, k, b):
    return k * x + b

lamb = 5461

d = np.array([
    7.30, 7.02, 6.81, 6.59,
    6.35, 6.06, 5.87, 5.59, 5.33,
    5.07, 4.74, 4.42, 4.03,
    3.65, 3.23, 2.69, 2.07, 1.20,
])

d_ = np.array([
    7.42, 7.13, 6.91, 6.70, 6.48,
    6.23, 5.98, 5.74, 5.46,
    5.19, 4.91, 4.57, 4.26, 3.87,
    3.46, 3.01, 2.41, 1.75
])

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))

# максимумы

x = np.array([36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2])
y = (d * 98.8 / 2) ** 2

plt.plot(x, y, 'k8', ms=5, label='максимумы')

coefs, pcov = curve_fit(func, x, y)
coef_error = np.sqrt(np.diag(pcov))
plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=fr'k = {round(coefs[0], 1)} $\pm$ {round(coef_error[0], 1)} мкм$^2$')
print(coefs, coef_error)

print('Радиус кривизны ', coefs[0] / lamb, ' мкм')

# минимумы

x = np.array([35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])
y = (d_ * 98.8 / 2) ** 2

plt.plot(x, y, 'k*', ms=5, label='минимумы')

coefs, pcov = curve_fit(func, x, y)
coef_error = np.sqrt(np.diag(pcov))
plt.plot(x, func(x, coefs[0], coefs[1]), 'g-', label=fr'k = {round(coefs[0], 1)} $\pm$ {round(coef_error[0], 1)} мкм$^2$')
print(coefs, coef_error)

print('Радиус кривизны ', coefs[0] / lamb, ' мкм')

plt.axhspan(ymin=-2952.8356, ymax=2952.8356, color='orange', alpha=0.7, label='Центральное тёмное пятно')

plt.xlabel(r'$m$')
plt.ylabel('$r^2$, мкм$^2$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()
ax.set_xticks(np.arange(36, -1, -2, int))

plt.savefig('image2.jpg')
