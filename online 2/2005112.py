import numpy as np
import matplotlib.pyplot as plt

def sort_array(x1, y1, value, m):
    for i in range(m):
        for j in range(i + 1, m):
            if ((np.abs(x1[i] - value)) >= np.abs(x1[j] - value)):
                x1[i], x1[j] = x1[j], x1[i]
                y1[i], y1[j] = y1[j], y1[i]


def lagrange(xp, x, y, n):
    yp = 0
    for i in range(n + 1):
        p = 1
        for j in range(n + 1):
            if j != i:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += y[i] * p
    return yp

x1 = np.array([])
y1 = np.array([])

file = open("stock.txt","r")
line1 = file.readline()
lines = file.readlines()
x1 = np.append(x1, [float(line.split()[0]) for line in lines])
y1 = np.append(y1, [float(line.split()[1]) for line in lines])

xp = int(input("Enter the value of x: "))

m = 5
n = m-1
sort_array(x1, y1, xp, x1.size)
print(x1)

x = np.array([])
for i in range(m):
    x = np.append(x, [x1[i]])

y = np.array([])
for i in range(m):
    y = np.append(y, [y1[i]])

yp = lagrange(xp, x, y, n)
print("For x = " + str(xp)+ " y = " + str(yp))
prev = lagrange(xp, x, y, n-1)
error = np.abs(((yp - prev)/yp)*100)
print("absolute approximate relative error : " + str(error))


xValues = np.arange(0, 200)
yValues = []

for i in range(0, 200):
    yValues.append(lagrange(i, x, y, n))

plt.plot(xValues, yValues, '-')
plt.plot(x1,y1)
plt.title("Approximate graph")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.scatter(xp, yp, c="red")
plt.show()