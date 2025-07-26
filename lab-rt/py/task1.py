from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

A0 = 81663

A = np.array([24302, 11646, 6234, 2366, 1191, 927, 687, 659, 662, 791])
f = np.array([50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000])

plt.rcParams.update({'font.size': 11})

x = np.log10(f)
y = 20 * np.log10(A)

def func(x, k, b):
    return k * x + b

coefs, pcov = curve_fit(func, x[:-3], y[:-3])
print(coefs[0])

# fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')
plt.plot([np.log10(5), np.log10(30)], [20*np.log10(A0), 20*np.log10(A0)], label=r'$A_0$')
plt.plot([np.log10(5), np.log10(30)], [20*np.log10(0.7*A0), 20*np.log10(0.7*A0)], label=r'$0.7 \cdot A_0$')
plt.plot([np.log10(5), np.log10(15000000)], [20*np.log10(1), 20*np.log10(1)], label=r'$1$')


x = np.log10(np.array([5, 20, 30, 50, 100, 200, 500, 1000, 2000, 10000000]))
plt.plot(x, func(x, coefs[0], coefs[1]), 'r-')
plt.ylabel(r'A_{дц}=$20\cdot \lg{A}$')
plt.xlabel(r'$\lg{f}$')
plt.title('Амплитудно-частотная характеристика ОУ')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

# ax.errorbar(x, y, yerr=np.sqrt(abs(y - (coefs[0] * x + coefs[1]))), fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image1.jpg')

# coef_error = np.sqrt(np.diag(pcov))
#
# print(coefs, coef_error)
