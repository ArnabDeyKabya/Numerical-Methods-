import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (-1) * (6.73*x + 6.725E-8+(7.26E-4)*(5E-4)) / (x*3.62E-12 + x*5E-4*3.908E-8)

a = 9.15E-5
b = 3.05E-5

n = int(input('Enter n: '))


def trapezoid_Integration(a, b, n):
    h = (b - a)/n

    ans = 0

    for i in range(1, n):
        ans += 2*f(a + i*h)

    ans = (h / 2) * (f(a) + ans + f(b))
    return ans



def Simpson_calculation(a, b):
    return ((b-a)/6) * (f(a) + 4*f((a+b) / 2) + f(b))


def simpson_Integration(a, b, n):
    h = (b-a)/n
    answer = Simpson_calculation(a, a+h)

    for i in range(1, n):
        answer += Simpson_calculation(a+i*h, a+(i+1)*h)

    return answer




print("Trapezoid rule result: ", trapezoid_Integration(a,b,n))
old_value = 0
new_value = 0
for i in range(1, n+1):
    if i == 1:
        new_value = trapezoid_Integration(a, b, i)
    else:
        old_value = new_value
        new_value = trapezoid_Integration(a, b, i)

        error1 = np.abs(((new_value-old_value)/new_value)*100)
        print("For Application "+ str(i)+" error is: "+ str(error1))
print()
print()




print("The intrigal Value for Simpsons' Rule is : ", simpson_Integration(a, b, n))
old = 0
new = 0
for i in range(1, n+1):
    if i==1:
        new = simpson_Integration(a, b, i)
    else:
        old = new
        new = simpson_Integration(a, b, i)
        error = np.abs(((new - old) / new) * 100)
        print("For Application "+ str(i) + " error is: "+ str(error))





x = [1.22E-4, 1.20E-4, 1.0E-4, 0.8E-4, 0.6E-4, 0.4E-4, 0.2E-4]

xAxis = np.array(x)
yAxis = simpson_Integration(1.22E-4, xAxis, 5)


plt.plot(xAxis, yAxis,  '--', marker='o')
plt.title("time vs. oxygen concentration")
plt.xlabel("x")
plt.ylabel("time(t)")
plt.show()