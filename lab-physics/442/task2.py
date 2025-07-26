from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from math import radians

plt.rcParams.update({'font.size': 15})


def func(x, k, b):
    return k * x + b


y = np.array([12.5, 25.3,]) * np.pi / 180 / 60
x = np.array([-1/0.622, -2/0.983])
x = np.array([1, 2])

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

coefs, pcov = curve_fit(func, x, y)
coef_error = np.sqrt(np.diag(pcov))
plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 3)} угл.сек./А')
print(coefs, coef_error)

plt.xlabel(r'$m$')
plt.ylabel('$D$, угл.сек./А')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image2.jpg')

