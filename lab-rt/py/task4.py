from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

Uin2 = np.array([27, 51, 89, 125, 179, 248, 345, 483, 651, 679, 587, 472, 374, 320, 275, 242, 216, 195, 178, 163])
Uin = Uin2 / 2
print(Uin)
f = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])

plt.rcParams.update({'font.size': 11})

x = f
y = Uin / max(Uin)

def func(x, k, b):
    return k * x + b

# coefs, pcov = curve_fit(func, x[:-3], y[:-3])
# print(coefs[0])
#
fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')
plt.plot([600, 1400], [0.7, 0.7], label=r'$0.7$')

plt.ylabel(r'$U/U_{max}$')
plt.xlabel(r'f, Гц')
plt.title('Амплитудно-частотная характеричтика фильтра')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

# # ax.errorbar(x, y, yerr=np.sqrt(abs(y - (coefs[0] * x + coefs[1]))), fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image4.jpg')
#
# # coef_error = np.sqrt(np.diag(pcov))
# #
# # print(coefs, coef_error)
