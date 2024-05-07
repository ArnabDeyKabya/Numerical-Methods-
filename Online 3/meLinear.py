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

"""
def specialLinearRegression(X, Y):
    n = X.shape[0]

    Sxy = 0
    Sxx = 0

    for i in range(n):
        Sxx += (X[i]*X[i])
        Sxy += (X[i]*Y[i])

    a = Sxy / Sxx

    print("Sxy = ", Sxy)
    print("Sxx = ", Sxx)

    return a
"""



x = [2,3,5,7,8,10,12,13,15,16]
y = [4.7,6.9,9.8,12.6,14.3,16.9,19.6,21.2,23.8,25.4]

X = np.array(x)


Y = np.array(y)


ans = linearRegression(X, Y)

print(ans[0], ans[1])

a1= ans[1]
a0= ans[0]

plt.scatter(X, Y, color="m", marker="o")


def f(x):
    return a1*x + a0


xValues = np.linspace(2,16,100)
yValues = f(xValues)

plt.plot(xValues, yValues,  '-r')
plt.show()

