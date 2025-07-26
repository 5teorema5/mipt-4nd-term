from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 13})

def func(x, k, b):
    return k * x + b


plt.rcParams.update({'font.size': 13})

d_sr = np.array([38.798, 35.174, 31.375, 26.917, 21.730, 14.730])
delta_d = np.array([1.111, 1.187, 1.302, 1.628, 2.040, 2.964])

x = 1 / delta_d
y = d_sr

coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 1)}, b = {round(coefs[1], 1)}')
plt.ylabel(r'Квадрат диаметра интерференционного кольца, $d^2$, $мм^2$')
plt.xlabel('Номер кольца, i')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

ax.errorbar(x, y, yerr=np.sqrt(abs(y - (coefs[0] * x + coefs[1]))), fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image2.jpg')

coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)
