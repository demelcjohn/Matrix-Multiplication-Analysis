import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def curve_func(x, a, b, c):
    return a * np.exp(-b * x) + c


data = []
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

n = []
iterativeTime = []
divConTime = []
strassenTime = []
for row in data:
    n.append(float(row['n']))
    iterativeTime.append(float(row['iterativeTime']))
    divConTime.append(float(row['divConTime']))
    strassenTime.append(float(row['strassenTime']))

mean_iterativeTime = np.mean(iterativeTime)
variance_iterativeTime = np.var(iterativeTime)
std_dev_iterativeTime = np.std(iterativeTime)

mean_divConTime = np.mean(divConTime)
variance_divConTime = np.var(divConTime)
std_dev_divConTime = np.std(divConTime)

mean_strassenTime = np.mean(strassenTime)
variance_strassenTime = np.var(strassenTime)
std_dev_strassenTime = np.std(strassenTime)


print("Mean of iterativeTime:", mean_iterativeTime)
print("Variance of iterativeTime:", variance_iterativeTime)
print("Standard deviation of iterativeTime:", std_dev_iterativeTime)
print()
print("Mean of divConTime:", mean_divConTime)
print("Variance of divConTime:", variance_divConTime)
print("Standard deviation of divConTime:", std_dev_divConTime)
print()
print("Mean of strassenTime:", mean_strassenTime)
print("Variance of strassenTime:", variance_strassenTime)
print("Standard deviation of strassenTime:", std_dev_strassenTime)
print()


params, _ = curve_fit(curve_func, n, iterativeTime)
x_curve = np.linspace(min(n), max(n), 600)
y_curve = curve_func(x_curve, *params)
plt.scatter(n, iterativeTime, label='iterativeTime')
# plt.plot(x_curve, y_curve, label='Fitted Curve')

params, _ = curve_fit(curve_func, n, divConTime)
x_curve = np.linspace(min(n), max(n), 100)
y_curve = curve_func(x_curve, *params)
plt.scatter(n, divConTime, label='divConTime')
# plt.plot(x_curve, y_curve, label='Fitted Curve')

params, _ = curve_fit(curve_func, n, strassenTime)
x_curve = np.linspace(min(n), max(n), 100)
y_curve = curve_func(x_curve, *params)
plt.scatter(n, strassenTime, label='strassenTime')
# plt.plot(x_curve, y_curve, label='Fitted Curve')

plt.xlabel('n')
plt.ylabel('time in sec')
plt.title('Matrix multiplication time comparison')
plt.legend()
plt.grid(True)
plt.show()
