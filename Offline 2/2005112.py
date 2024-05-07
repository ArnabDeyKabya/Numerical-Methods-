import numpy as np
n = int(input("Enter The number of variables: "))

matrix = []
for i in range(0, n):
    temp_matrix = []
    for j in range(0, n):
        x = float(input())
        temp_matrix.append(x)
    matrix.append(temp_matrix)
A = np.array(matrix)

constant_matrix = []
for i in range(0, n):
    y = float(input())
    constant_matrix.append(y)
B = np.array(constant_matrix)
print()

print("A is: ")
print(A)
print()
print("B is: ")
print(B)
print()
print("The Sub Steps Are: ")


def GaussianElimination(A, B, pivot=True, showall=True):
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

                if showall:
                    print("A matrix is: ")
                    np.set_printoptions(precision=4, suppress=True)
                    print(A)
                    print()
                    print("B matrix is : ")
                    np.set_printoptions(precision=4, suppress=True)
                    print(B)
                    print()

    answer[n - 1] = B[n - 1] / A[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        temp = B[i]
        for m in range(n - 1, i, -1):
            temp -= answer[m] * A[i][m]

        answer[i] = temp / A[i][i]
    if(showall):
        determinant = np.linalg.det(A)
        print("The determinant of the coefficient matrix A at the end of the Gaussian Elimination: " + f'{determinant:4f}')
    return answer



answer_matrix = GaussianElimination(A, B)

print("The Required Answer is: ")
for ans in answer_matrix:
    print(f'{ans:.4f}')

"""
Sample input 1: 
3
25
5
1
64
8
1
144
12
1
106.8
177.2
279.2
"""
"""
Sample input 2:
 3
20
15
10
-3
-2.249
7
5
1
3
45
1.751
9
"""
