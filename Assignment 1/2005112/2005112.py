import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return ((x**3) - (0.18*x*x) + (0.0004752))
def diff_f(x):
     return 3*x*x - 0.36*x

"""
def bisection_method(lower, upper, approx, max_iter):
    temp = (lower + upper)/2
    error = 100
    print("This is for Bisection Method: ")
    for i in range(0, max_iter):
        mid_value = (lower + upper)/2
        if i!= 0:
            error = np.abs(((mid_value - temp)/mid_value)*100)
        print("For Iteration "+ str(i +1) + " Error is: " + str(error) )

        if(f(lower)*f(mid_value)<0):
            upper = mid_value
        elif(f(lower)*f(mid_value) > 0):
            lower = mid_value
        else:
            return mid_value
        if(error <= approx):
            return mid_value

        temp = mid_value
    return mid_value

"""
def bisection_method(low, up, app, iter):
    temp = (up + low)/2
    error = 100
    for i in range(0, iter):
        mid = (up + low)/2
        if i!=0:
            error = np.abs(((mid - temp)/mid)*100)
        elif(f(low) * f(mid) < 0):
            up = mid
        if(f(low) * f(mid) > 0):
            low = mid
        else:
            return mid
        if(error <= app):
            return mid
        temp = mid
    return mid

def newton_raphson_method(initial, relative_approx, iter):
    old_value = initial
    error = 100
    print("This is for Newton Raphson Method: ")
    for i in range(0, iter):
        new_value = old_value - (f(old_value) / diff_f(old_value))
        error = np.abs(((new_value - old_value) / new_value) * 100)
        print("For Iteration "+ str(i +1) + " Error is: " + str(error) )
        if (error <= relative_approx):
            break
        old_value = new_value
    return  new_value

xAxis = np.linspace(-0.1, 0.25, 900)
yAxis = f(xAxis)
plt.plot(xAxis, yAxis, '-r')
plt.title("Graph for finding the approximate location of the root")
plt.grid()
plt.xlabel("x (m)")
plt.ylabel("f(x)")
plt.show()




print("The approximate value of the root by Bisection Method is: ", bisection_method(0, 0.12, 0.5, 20))
print()
print("The approximate value of the root By Newton Raphson Method is: ", newton_raphson_method(0.06, 0.5, 20))

