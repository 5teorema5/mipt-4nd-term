from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 13})

def func(x, k):
    return k * x


m = np.array([6, 5, 4, 3, 2])
# z = np.log(np.array([11.1, 11.4, 11.7, 12.5, 13.5]) * 10)
z = np.array([1.3, 1.6, 1.9, 2.7, 3.7]) * 10

x = 1/m
y = z

coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0]), 'r-', label=f'k = ({round(coefs[0], 1)}$\pm${round(np.sqrt(np.diag(pcov))[0], 1)}) мм')
plt.ylabel(r'Расстояние до щели z, мм')
plt.xlabel(r'Число обратное числу открытых зон Френеля, $\frac{1}{m}$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
ax.errorbar(x, y, yerr=abs(y - (coefs[0] * x)), fmt='.', linewidth=2, capsize=6)

# ax.errorbar(x, y, yerr=[np.sqrt(np.diag(pcov))[1] for i in range(len(x))], fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image3.jpg')

coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)
