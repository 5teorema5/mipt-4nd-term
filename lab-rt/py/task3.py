from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

A0 = 81663

Uin2 = np.array([38, 39, 38, 38, 38, 38, 38, 37, 31, 20, 11, 7])
Uin = Uin2 / 2
K = Uin / 20
print(K)
f = np.array([2, 5, 10, 20, 50, 100, 500, 1000, 2000, 3000, 4000, 5000])

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
plt.plot([0, 5000], [0.675, 0.675], label=r'$0.7 \cdot K_0$')
# plt.plot([0, 500000], [1, 1], label=r'$1$')

plt.ylabel(r'K')
plt.xlabel(r'f, кГц')
plt.title('Зависимость от частоты коэффициента усиления (ОУ по схеме повторителя)')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

# # ax.errorbar(x, y, yerr=np.sqrt(abs(y - (coefs[0] * x + coefs[1]))), fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image3.jpg')
#
# # coef_error = np.sqrt(np.diag(pcov))
# #
# # print(coefs, coef_error)
