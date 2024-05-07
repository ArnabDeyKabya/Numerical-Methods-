import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (1.37 - (1/x))
def diff_f(x):
     return (x**(-2))





def newton_raphson_method(initial, relative_approx, iter):
    old_value = initial
    error = 100
    for i in range(0, iter):
        new_value = old_value - (f(old_value) / diff_f(old_value))
        error = np.abs(((new_value - old_value) / new_value) * 100)
        if (error <= relative_approx):
            break
        old_value = new_value
    return  new_value



xAxis = np.linspace(0, 0.8, 900)
yAxis = f(xAxis)
plt.plot(xAxis, yAxis, '-r')
plt.grid()
plt.xlabel("y")
plt.ylabel("f(x)")
plt.show()

print("The approximate value of the root ", newton_raphson_method(0.01, 0.05, 200))