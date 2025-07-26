from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k):
    return k * x


plt.rcParams.update({'font.size': 13})

# мкм
x_m_1 = np.array([-472, -304, -156, 0, 160, 312, 476, ])
m_1 = np.array([-3, -2, -1, 0, 1, 2, 3, ])
x_m_2 = np.array([-480, -244, 0, 224, 492, ])
m_2 = np.array([-2, -1, 0, 1, 2, ])
x_m_3 = np.array([-436, 0, 496, ])
m_3 = np.array([-1, 0, 1, ])
x_m_4 = np.array([-1036, -516, 0, 592, 1048, ])
m_4 = np.array([-2, -1, 0, 1, 2, ])
x_m_5 = np.array([-840, 0, 836, ])
m_5 = np.array([-1, 0, 1, ])

# МГц
nu = [1.15371, 1.82893, 3.468, 3.958, 6.295]

# 1

x = m_1
y = x_m_1
coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0]), 'r-', label=f'k = {round(coefs[0], 1)}')
plt.ylabel('Порядок дифракционного максимума, m')
plt.xlabel('Координата дифракционного максимума, $x_m$, мкм')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

ax.errorbar(x, y, yerr=abs(y - (coefs[0] * x)), fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image1.jpg')

coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)

# 2

x = m_2
y = x_m_2
coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0]), 'r-', label=f'k = {round(coefs[0], 1)}')
plt.ylabel('Порядок дифракционного максимума, m')
plt.xlabel('Координата дифракционного максимума, $x_m$, мкм')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

ax.errorbar(x, y, yerr=abs(y - (coefs[0] * x)), fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image2.jpg')

coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)

# 3

x = m_3
y = x_m_3
coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0]), 'r-', label=f'k = {round(coefs[0], 1)}')
plt.ylabel('Порядок дифракционного максимума, m')
plt.xlabel('Координата дифракционного максимума, $x_m$, мкм')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

ax.errorbar(x, y, yerr=abs(y - (coefs[0] * x)), fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image3.jpg')

coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)

# 4

x = m_4
y = x_m_4
coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0]), 'r-', label=f'k = {round(coefs[0], 1)}')
plt.ylabel('Порядок дифракционного максимума, m')
plt.xlabel('Координата дифракционного максимума, $x_m$, мкм')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

ax.errorbar(x, y, yerr=abs(y - (coefs[0] * x)), fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image4.jpg')

coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)

# 5

x = m_5
y = x_m_5
coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0]), 'r-', label=f'k = {round(coefs[0], 1)}')
plt.ylabel('Порядок дифракционного максимума, m')
plt.xlabel('Координата дифракционного максимума, $x_m$, мкм')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()

ax.errorbar(x, y, yerr=abs(y - (coefs[0] * x)), fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image5.jpg')

coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)
