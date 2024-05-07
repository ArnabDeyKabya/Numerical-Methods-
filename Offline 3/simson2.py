from pickle import TRUE


def simpleSimpson(a, b, show):

    if(show):
        print("f(", a, ") = ",  f(a), " ----- ", "f(", (a+b)/2, ") = ",
              f((a+b)/2), " ------- ", "f(", b, ") = ",  f(b))
    return ((b-a)/6) * (f(a) + 4*f((a+b) / 2) + f(b))


def simpsonIntegration(a, b, n, show=True):
    h = (b-a)/n

    print("( 0 , 1 )   : ", end=" ")
    result = simpleSimpson(a, a+h, show)

    for i in range(1, n):
        print("(", i, ",", i+1, ") ", " : ", end=" ")
        result += simpleSimpson(a+i*h, a+(i+1)*h, show)

    return result


def totalSimpson(a, b, n):
    h = (b - a)/n

    result = f(a) + f(b)

    print("0: f(", a, ") = ",  f(a))

    for i in range(1, n):

        print(i, ": f(", a+i*h, ") = ",  f(a+i*h))

        if i % 2 != 0:
            result += 4*f(a+i*h)
        else:
            result += 2*f(a+i*h)

    result = (h/3)*result

    return result


def f(x):
    return (-1) * (6.73*x + 6.725E-8+(7.26E-4)*(5E-4)) / (x*3.62E-12 + x*5E-4*3.908E-8)


a = 1.22E-4
b = a / 2

n = 5

print("Check with Simple Simpson: ")

print(simpsonIntegration(a, b, n))

print("Check --- ", totalSimpson(a, b, 2*n))
