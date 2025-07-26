from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

A0 = 81663

Uin2 = np.array([1.842, 1.864, 1.894, 1.893, 1.898, 1.9, 1.899, 1.77, 1.53, 0.92, 0.51, 0.26, 0.103])
Uin = Uin2 / 2
K = Uin / 0.02
print(K)
f = np.array([10, 20, 50, 100, 200, 500, 1000, 10000, 20000, 50000, 100000, 200000, 500000])

plt.rcParams.update({'font.size': 11})

x = f
y = K

def func(x, k, b):
    return k * x + b

# coefs, pcov = curve_fit(func, x[:-3], y[:-3])
# print(coefs[0])
#
fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')
plt.plot([0, 500000], [32.725, 32.725], label=r'$0.7 \cdot K_0$')
plt.plot([0, 500000], [1, 1], label=r'$1$')

plt.ylabel(r'K')
plt.xlabel(r'f, Гц')
plt.title('Зависимость от частоты коэффициента усиления')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

# # ax.errorbar(x, y, yerr=np.sqrt(abs(y - (coefs[0] * x + coefs[1]))), fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image2.jpg')
#
# # coef_error = np.sqrt(np.diag(pcov))
# #
# # print(coefs, coef_error)
