from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from math import radians

plt.rcParams.update({'font.size': 15})


def dms_to_dd(degrees, minutes, seconds):
    return np.radians(degrees + minutes / 60 + seconds / 3600)


def func(x, k, b):
    return k * x + b

tmp = dms_to_dd(90, 16, 57)
phi_g = np.array([107, 107, 108, 111, 111, 113, 114, 114, 116])
phi_m = np.array([34, 42, 46, 14, 0, 19, 12, 17, 14])
phi_s = np.array([8, 25, 26, 4, 51, 32, 41, 4, 18])

y = np.sin(radians(90)-dms_to_dd(phi_g, phi_m, phi_s)-tmp-radians(45))

# y = np.sin(dms_to_dd(phi_g, phi_m, phi_s))
x = np.array([4230, 4330, 4456, 4916, 4999, 5461, 5770, 5791, 6234])

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

coefs, pcov = curve_fit(func, x, y)
coef_error = np.sqrt(np.diag(pcov))
plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=rf'k = {round(coefs[0], 8)*10**7} $\pm$ {round(coef_error[0], 7)*10**7} шт/мм')
print(coefs, coef_error)

plt.xlabel(r'$\lambda$, $\mathring{А}$')
plt.ylabel('$sin(φ)$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image1.jpg')

