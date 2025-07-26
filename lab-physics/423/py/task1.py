from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})


def func(x, k, b):
    return k * x + b


t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
z = np.array([10.245, 9.275, 8.565, 8.15, 7.475, 6.165, 5.885, 5.625, 5.415, 5.275])

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))

x = t
y = z

plt.plot(x, y, 'k8', ms=5, label='максимумы')

coefs, pcov = curve_fit(func, x, y)
coef_error = np.sqrt(np.diag(pcov))

plt.xlabel(r'$z$')
plt.ylabel('t, мин')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image1.jpg')
