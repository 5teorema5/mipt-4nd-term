from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 13})

def func(x, k, b):
    return k * x + b


x_m = np.array([3.6, 3.8, 4.1, 4.3, 4.5, 4.8, 5, 5.2, 5.4, 5.7, 5.9, 6.2]) * 10 * 0.04
m = np.array([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

x = m
y = x_m
print(y)

coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = ({round(coefs[0], 3)}$\pm${round(np.sqrt(np.diag(pcov))[0], 3)}) мм')
plt.ylabel(r'Положения экстремумов, $x_m$, $мм$')
plt.xlabel('Номер экстремума, m')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

ax.errorbar(x, y, yerr=[np.sqrt(np.diag(pcov))[1] for i in range(len(x))], fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image5.jpg')

coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)
