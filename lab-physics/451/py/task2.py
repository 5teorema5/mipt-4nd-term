from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

ampl_40 = np.array([2.88, 2.905, 2.799, 2.805, 2.79, 2.904, 2.871, 2.837, 2.836, 2.843, 2.714,])
sr_40 = ampl_40.sum()/ampl_40.size
ampl_50 = np.array([3.76, 3.599, 3.469, 3.752, 3.729, 3.729, 3.61, 3.678, 3.669, 3.771, 3.569,])
sr_50 = ampl_50.sum()/ampl_50.size
ampl_60 = np.array([4.285, 4.307, 4.316, 4.426, 4.473, 4.415, 4.539, 4.477, 4.472, 4.508, 4.364,])
sr_60 = ampl_60.sum()/ampl_60.size
ampl_70 = np.array([6.004, 6.104, 6.161, 6.008, 6.232, 6.293, 6.518, 6.352, 6.54, 5.965, 6.471,])
sr_70 = ampl_70.sum()/ampl_70.size
ampl_80 = np.array([7.052, 7.307, 7.412, 7.093, 7.047, 7.183, 7.134, 6.847, 7.263, 7.051, 7.123,])
sr_80 = ampl_80.sum()/ampl_80.size
ampl_90 = np.array([7.443, 7.334, 7.317, 7.412, 7.145, 7.459, 7.171, 7.311, 7.205, 7.361, 7.446,])
sr_90 = ampl_90.sum()/ampl_90.size
ampl_100 = np.array([6.441, 6.363, 6.434, 6.443, 6.724, 6.367, 6.463, 6.451, 6.459, 6.457, 6.478,])
sr_100 = ampl_100.sum()/ampl_100.size
ampl_110 = np.array([5.342, 5.181, 5.312, 5.304, 5.374, 5.408, 5.175, 5.325, 5.285, 5.288, 5.274,])
sr_110 = ampl_110.sum()/ampl_110.size
ampl_120 = np.array([3.756, 3.819, 3.832, 3.787, 3.757, 3.751, 3.971, 3.687, 3.762, 3.835, 3.786,])
sr_120 = ampl_120.sum()/ampl_120.size
ampl_130 = np.array([3.048, 3.055, 3.054, 3.046, 3.077, 3.058, 3.104, 3.031, 3.006, 3.075, 3.113,])
sr_130 = ampl_130.sum()/ampl_130.size
ampl_140 = np.array([2.059, 2.026, 1.956, 2.027, 2.021, 2.046, 2.012, 2.021, 2.022, 2.028, 2.083,])
sr_140 = ampl_140.sum()/ampl_140.size

x = np.array([40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140])
y = np.array([sr_40, sr_50, sr_60, sr_70, sr_80, sr_90, sr_100, sr_110, sr_120, sr_130, sr_140])

for i in range(x.size):
    print(fr'{x[i]} & {round(y[i], 3)} \\ \hline')

y = y ** 2

coefficients = np.polyfit(x, y, 7)
fx = np.linspace(x[0], x[-1])
fy = np.polyval(coefficients, fx)

max_fy = max(fy)
y = y / max_fy
fy = fy / max_fy

plt.rcParams.update({'font.size': 11})

def func(x, k, b):
    return k * x + b

coefs, pcov = curve_fit(func, x, y)

# fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')
plt.plot(fx, fy, '-', ms=5)

# plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 1)}, b = {round(coefs[1], 1)}')
plt.ylabel(r'Относительная интенсивность, $I/I_0$')
plt.xlabel('Угол поворота поляроида, град.')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

# ax.errorbar(x, y, yerr=np.sqrt(abs(y - (coefs[0] * x + coefs[1]))), fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image2.jpg')

# coef_error = np.sqrt(np.diag(pcov))
#
# print(coefs, coef_error)
