import numpy as np
import matplotlib.pyplot as plt


def linearRegression(X, Y):
    n = X.shape[0]

    Sxy = 0
    Sx = 0
    Sy = 0
    Sxx = 0

    for i in range(n):
        Sx += (X[i])
        Sy += (Y[i])
        Sxy += (X[i]*Y[i])
        Sxx += (X[i]*X[i])
    b = ((n*Sxy) - (Sx * Sy)) / ((n*Sxx) - (Sx*Sx))
    xMean = Sx / n
    yMean = Sy / n
    a = yMean - b * xMean
    return (a, b)


x = [0.04, 0.07, 1.4, 2.3, 2.9, 3.6, 4.1]
y = [3.3E-7, 5.76E-6, 20.41, 275.81, 900, 2600.76, 5150.46]


X = np.array(x)
Y = np.array(y)

Z = np.log(Y)
X1 = np.log(X)


ans = linearRegression(X1, Z)
print(ans)

A = np.exp(ans[0])
B = ans[1]

print(A, B)


plt.scatter(X, Y, color="m", marker="o")


def f(x):
    return A*(x**B)


xValues = np.linspace(0,5,100)
yValues = f(xValues)
plt.plot(xValues, yValues,  '-r')
plt.show()