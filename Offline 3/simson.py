from gettext import npgettext
from unittest import result
import numpy as np
import matplotlib.pyplot as plt

a = 1.22E-4
b = a / 2


def f(x):
    return (-1) * (6.73*x + 6.725E-8+(7.26E-4)*(5E-4)) / (x*3.62E-12 + x*5E-4*3.908E-8)


def trapezoidIntegration(a, b, n):
    h = (b - a)/n

    result = 0

    for i in range(1, n):
        result += 2*f(a + i*h)

    result = (h / 2) * (f(a) + result + f(b))

    return result


def simpleSimpson(a, b):
    return ((b-a)/6) * (f(a) + 4*f((a+b) / 2) + f(b))


def simpsonIntegration(a, b, n):
    h = (b-a)/n

    result = simpleSimpson(a, a+h)

    for i in range(1, n):
        result += simpleSimpson(a+i*h, a+(i+1)*h)

    return result


n = int(input('Enter n: '))

# Number 1 Ques

print(f'\nTrapezoidal rule result: {trapezoidIntegration(a, b, n)} \n')

print("\t\t\tTrapezoid Rule AARE Table")
print("\t Value \t\t\t\t\t\t ARAE")

old = 0
new = 0

for n in range(1, 6):
    if n == 1:
        new = trapezoidIntegration(a, b, n)
        print(f"\t{new} \t\t\t\t N\A")
    else:
        old = new
        new = trapezoidIntegration(a, b, n)

        absError = abs((new-old)/new)*100
        print(f"\t{new} \t\t\t\t {absError}%")


# Number 2 Ques

print(f'\n\nSimpson rule result: {simpsonIntegration(a, b, n)}\n')


print("\t\t\tSimpsom Rule AARE Table")
print("\t Value \t\t\t\t\t\t ARAE")
old = 0
new = 0

for n in range(1, 6):
    if n == 1:
        new = simpsonIntegration(a, b, n)
        print(f"\t{new} \t\t\t\t N\A")
    else:
        old = new
        new = simpsonIntegration(a, b, n)

        absError = abs((new-old)/new)*100
        print(f"\t{new} \t\t\t\t {absError}%")

# Number 3 Ques

x = [1.22E-4, 1.20E-4, 1.0E-4, 0.8E-4, 0.6E-4, 0.4E-4, 0.2E-4]

xValues = np.array(x)
yValues = simpsonIntegration(a, xValues, 5)


plt.plot(xValues, yValues,  '--', marker='o')
plt.title("time vs. oxygen concentration")
plt.xlabel("x")
plt.ylabel("t")
plt.show()