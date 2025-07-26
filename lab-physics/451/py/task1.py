from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

eff_ch_1_0 = np.array([72.177, 72.002, 71.351, 71.620, 71.559, 71.284, 71.576, 71.622, 71.403, 71.646, 71.575, ])
eff_ch_2_0 = np.array([46.412, 46.254, 45.669, 45.978, 45.888, 45.640, 45.914, 45.961, 45.809, 45.955, 45.898, ])
for i in range(eff_ch_2_0.size):
    print(fr'{i+1} & {eff_ch_2_0[i]} \\ \hline')
sr_eff_ch = eff_ch_1_0/eff_ch_2_0
sr_0 = sr_eff_ch.sum()/sr_eff_ch.size

eff_ch_1_20 = np.array([70.219, 69.897, 69.898, 69.715, 69.913, 69.765, 69.647, 69.690, 69.173, 69.386, 68.757, ])
eff_ch_2_20 = np.array([46.096, 45.848, 45.902, 45.721, 45.909, 45.817, 45.782, 45.725, 45.387, 45.526, 45.093, ])
sr_eff_ch = eff_ch_1_20/eff_ch_2_20
sr_20 = sr_eff_ch.sum()/sr_eff_ch.size

# eff_ch_1_45 = np.array([71.046, 71.188, 71.283, 70.974, 71.048, 71.167, 71.018, 70.804, 70.722, 70.465, 70.684, ])
# eff_ch_2_45 = np.array([45.538, 45.655, 45.756, 45.557, 45.552, 45.677, 45.466, 45.415, 45.386, 45.134, 45.323, ])
# sr_eff_ch = eff_ch_1_45/eff_ch_2_45
# sr_45 = sr_eff_ch.sum()/sr_eff_ch.size

eff_ch_1_52 = np.array([70.916, 70.849, 70.363, 70.330, 70.436, 70.544, 70.493, 70.723, 70.740, 70.499, 70.585, ])
eff_ch_2_52 = np.array([46.724, 46.732, 46.453, 46.376, 46.490, 46.515, 46.492, 46.609, 46.675, 46.590, 46.544, ])
for i in range(eff_ch_2_52.size):
    print(fr'{i+1} & {eff_ch_2_52[i]} \\ \hline')
sr_eff_ch = eff_ch_1_52/eff_ch_2_52
sr_52 = sr_eff_ch.sum()/sr_eff_ch.size

eff_ch_1_54 = np.array([69.834, 69.749, 69.652, 69.635, 69.733, 69.547, 69.758, 69.602, 70.045, 69.818, 69.716, ])
eff_ch_2_54 = np.array([46.174, 46.293, 46.397, 46.290, 46.099, 45.997, 46.024, 45.967, 45.849, 45.974, 45.830, ])
sr_eff_ch = eff_ch_1_54/eff_ch_2_54
sr_54 = sr_eff_ch.sum()/sr_eff_ch.size

print(f'ток 0 мА: {round(sr_0, 3)}')
print(f'ток 20 мА: {round(sr_20, 3)} -> {round(sr_20 / sr_0, 3)}')
# print(f'ток 45 мА: {round(sr_45, 3)}')
print(f'ток 52 мА: {round(sr_52, 3)} -> {round(sr_52 / sr_0, 3)}')
print(f'ток 54 мА: {round(sr_54, 3)} -> {round(sr_52 / sr_0, 3)}')

print(round(eff_ch_2_0.sum()/eff_ch_2_0.size, 3), max(eff_ch_2_0), min(eff_ch_2_0))
print(round(eff_ch_2_52.sum()/eff_ch_2_52.size, 3), max(eff_ch_2_52), min(eff_ch_2_52))
tmp_arr_20 = eff_ch_2_20 / eff_ch_2_0
tmp_arr_52 = eff_ch_2_52 / eff_ch_2_0
tmp_arr_54 = eff_ch_2_54 / eff_ch_2_0

print(round(tmp_arr_20.sum()/tmp_arr_20.size, 3))
print(round(tmp_arr_52.sum()/tmp_arr_52.size, 3))
print(round(tmp_arr_54.sum()/tmp_arr_54.size, 3))
