from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 13})

def func(x, k, b):
    return k * x + b


plt.rcParams.update({'font.size': 13})

d = np.array([37.896, 34.472, 30.705, 26.534, 21.391, 14.565])
dqrt = d ** 2
i = np.array([1, 2, 3, 4, 5, 6])
f = 120

x = i
y = dqrt

coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 1)}, b = {round(coefs[1], 1)}')
plt.ylabel('Квадрат диаметра интерференционного кольца, $d^2$, $мм^2$')
plt.xlabel('Номер кольца, i')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

# ax.errorbar(x, y, yerr=[np.sqrt(np.diag(pcov))[1] for i in range(len(x))], fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image1.jpg')

# coef_error = np.sqrt(abs(y**2 - (coefs[0] * x)**2))
# coef_error = np.sqrt(np.diag(pcov))

# print(coefs, coef_error)
