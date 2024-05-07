import numpy as np
import matplotlib.pyplot as plt

x = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]
y = [10.3, 13.5, 13.9, 14.2, 11.6, 10.3, 9.7, 9.6, 14.1, 19.8, 31.1]

X = np.array(x,dtype=np.longdouble)
Y = np.array(y,dtype=np.longdouble)

m = 3
n= m+1
def helper(i, j, X):
    sum = 0
    s = X.shape[0]
    for p in range(0, s):
        pro = X[p]**(i+j)
        sum += pro
    return sum

def helper2(i, X, Y):
    sum = 0
    s = X.shape[0]
    for p in range(0, s):
        pro = (X[p]**i)*Y[p]
        sum += pro
    return sum



matrix = np.zeros((n, n), np.longdouble)
matrix[0][0] = X.shape[0]

for i in range(0, n):
    for j in range(0, n):
        if( j != 0):
            matrix[i][j] = helper(i, j, X)


for j in range(1, n):
    matrix[j][0] = helper(j, 0, X)

constant_matrix = np.zeros((n))
for i in range(0, n):
    constant_matrix[i]= helper2(i, X, Y)

A = np.array(matrix)
B = np.array(constant_matrix)




def GaussianElimination(A, B, pivot=True):
    size = A.shape[0]
    answer = np.zeros(size)
    for i in range(0, size-1):
        if pivot:
            maximum_row = i
            for j in range(i+1, n):
                if np.abs(A[j][i]) > np.abs(A[maximum_row][i]):
                    maximum_row = j

            if maximum_row != i:
                for x in range(0, n):
                    A[i][x],A[maximum_row][x] = A[maximum_row][x],A[i][x]

                B[i],B[maximum_row] = B[maximum_row],B[i]

            for row in range(i + 1, n):
                factor = A[row][i] / A[i][i]

                for column in range(i, n):
                    A[row][column] = A[row][column] - factor * A[i][column]

                B[row] = B[row] - factor * B[i]

    answer[n - 1] = B[n - 1] / A[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        temp = B[i]
        for m in range(n - 1, i, -1):
            temp -= answer[m] * A[i][m]

        answer[i] = temp / A[i][i]
    return answer

a = GaussianElimination(A, B)


print(a)

plt.scatter(X, Y, color="m", marker="o")

def f(x):
    return (a[0] + a[1]*x + a[2]*(x**2) + a[3]*(x**3))



xValues = np.linspace(1900,2000,100)
yValues = f(xValues)
plt.plot(xValues, yValues,  '-r')
plt.show()



