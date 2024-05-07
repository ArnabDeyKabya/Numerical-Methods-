import numpy as np
import matplotlib.pyplot as plt


def linearRegression(X, Y):
    n = X.shape[0]

    S_xy = 0
    S_x = 0
    S_y = 0
    S_xx = 0
    for i in range(n):
        S_x += (X[i])
        S_y += (Y[i])
        S_xy += (X[i]*Y[i])
        S_xx += (X[i]*X[i])
    b = ((n*S_xy) - (S_x * S_y)) / ((n*S_xx) - (S_x*S_x))
    x_Mean = S_x / n
    y_Mean = S_y / n
    a = y_Mean - b * x_Mean
    return (a, b)


x = [0.5, 0.8, 1.5, 2.5, 4.0]
y = [1.1, 2.4, 5.3, 7.6, 8.9]


X = np.array(x)
Y = np.array(y)

Z = 1/Y
X1 = 1/(X**2)


ans = linearRegression(X1, Z)

A1 = ans[0]
B = (ans[1])/A1
A=1/A1

print("A: "+ str(A))
print("B: "+ str(B))


plt.scatter(X, Y, color="m", marker="o")


def f(x):
    return (A*(x**2))/(B+(x**2))

plt.scatter(2.0, f(2.0), color="g", marker="o")
plt.scatter(4.5, f(4.5), color="g", marker="o")

print("Value at x = 2.0 : "+ str(f(2.0)))
print("Value at x = 4.5 : "+ str(f(4.5)))


xValues = np.linspace(0.5,4.8,10000)
yValues = f(xValues)
plt.plot(xValues, yValues,  '-r')
plt.show()